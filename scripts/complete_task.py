#!/usr/bin/env python3
"""Mark a task as complete in docs/plan.md by task number."""

import re
import sys
from pathlib import Path

INCOMPLETE_TASK_RE = re.compile(r"^(\s*- \[) \] (\d+)(\..*)")


def complete(text: str, task_number: int) -> tuple[str, bool]:
    """Return (updated text, whether the task was found and marked)."""
    lines = text.splitlines(keepends=True)
    new_lines: list[str] = []
    found = False
    for line in lines:
        m = INCOMPLETE_TASK_RE.match(line.rstrip("\n"))
        if m and int(m.group(2)) == task_number:
            new_lines.append(f"{m.group(1)}x] {m.group(2)}{m.group(3)}\n")
            found = True
        else:
            new_lines.append(line)
    return "".join(new_lines), found


def main(plan_file: Path = Path("docs/plan.md")) -> None:
    if len(sys.argv) != 2:
        print("Usage: complete_task.py <task-number>", file=sys.stderr)
        sys.exit(1)
    try:
        task_number = int(sys.argv[1])
    except ValueError:
        print("Error: task-number must be an integer", file=sys.stderr)
        sys.exit(1)
    text = plan_file.read_text()
    new_text, found = complete(text, task_number)
    if found:
        plan_file.write_text(new_text)
        print(f"Task {task_number} marked as complete.")
    else:
        print(f"Task {task_number} not found or already complete.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
