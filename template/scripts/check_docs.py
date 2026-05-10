#!/usr/bin/env python3
"""Check docs/architecture.md and docs/plan.md for common issues.

Checks:
  architecture.md — required sections present and non-empty, no TBD markers
  plan.md         — tasks sequentially numbered, no TBD markers
"""

import re
import sys
from pathlib import Path

REQUIRED_ARCH_SECTIONS = [
    "Overview & Goals",
    "Tech Stack",
    "System Components",
    "Data Model",
]

TASK_RE = re.compile(r"^\s*- \[[ x]\] (\d+)\. ")
TBD_RE = re.compile(r"\bTBD\b", re.IGNORECASE)


def _section_has_content(lines: list[str], section: str) -> bool:
    """Return True if the ## section has at least one non-blank, non-header line."""
    inside = False
    for line in lines:
        if line.startswith("## ") and section in line:
            inside = True
            continue
        if inside:
            if line.startswith("## "):
                break
            if line.strip() and not line.startswith("#"):
                return True
    return False


def check_architecture(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path}: file not found"]
    lines = path.read_text().splitlines()

    for section in REQUIRED_ARCH_SECTIONS:
        if not any(line.startswith("## ") and section in line for line in lines):
            errors.append(f"architecture.md: missing required section '{section}'")
        elif not _section_has_content(lines, section):
            errors.append(f"architecture.md: section '{section}' is empty")

    for i, line in enumerate(lines, 1):
        if TBD_RE.search(line):
            errors.append(f"architecture.md:{i}: unresolved TBD: {line.strip()!r}")

    return errors


def check_plan(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path}: file not found"]
    lines = path.read_text().splitlines()

    task_numbers: list[tuple[int, int]] = []
    for i, line in enumerate(lines, 1):
        m = TASK_RE.match(line)
        if m:
            task_numbers.append((i, int(m.group(1))))

    expected = 1
    for line_no, task_no in task_numbers:
        if task_no != expected:
            errors.append(
                f"plan.md:{line_no}: numbering error — expected {expected},"
                f" got {task_no}"
            )
        expected = task_no + 1

    for i, line in enumerate(lines, 1):
        if TBD_RE.search(line):
            errors.append(f"plan.md:{i}: unresolved TBD: {line.strip()!r}")

    return errors


def main(docs_dir: Path = Path("docs")) -> None:
    errors = check_architecture(docs_dir / "architecture.md") + check_plan(
        docs_dir / "plan.md"
    )

    if errors:
        for error in errors:
            print(f"FAIL  {error}", file=sys.stderr)
        sys.exit(1)

    print("OK  docs check passed")


if __name__ == "__main__":
    main()
