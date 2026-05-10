#!/usr/bin/env python3
"""Renumber all tasks in docs/plan.md sequentially across all phases."""

import re
from pathlib import Path

TASK_RE = re.compile(r"^(\s*- \[[ x]\] )\d+\. (.+)$")


def renumber(text: str) -> tuple[str, int]:
    """Return (renumbered text, count of tasks found)."""
    lines = text.splitlines(keepends=True)
    counter = 1
    new_lines: list[str] = []
    for line in lines:
        m = TASK_RE.match(line.rstrip("\n"))
        if m:
            new_lines.append(f"{m.group(1)}{counter}. {m.group(2)}\n")
            counter += 1
        else:
            new_lines.append(line)
    return "".join(new_lines), counter - 1


def main(plan_file: Path = Path("docs/plan.md")) -> None:
    text = plan_file.read_text()
    new_text, count = renumber(text)
    plan_file.write_text(new_text)
    print(f"Renumbered {count} tasks.")


if __name__ == "__main__":
    main()
