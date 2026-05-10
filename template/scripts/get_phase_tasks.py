#!/usr/bin/env python3
"""List all tasks for a phase in docs/plan.md."""

import re
import sys
from pathlib import Path

PHASE_HEADER_RE = re.compile(r"^## Phase", re.IGNORECASE)
SECTION_RE = re.compile(r"^## ")
TASK_RE = re.compile(r"^\s*- \[([ x])\] (\d+\. .+)$")


def get_tasks(text: str, phase_query: str) -> list[tuple[bool, str]]:
    """Return list of (completed, description) for tasks in the matching phase."""
    lines = text.splitlines()
    in_phase = False
    tasks: list[tuple[bool, str]] = []
    phase_lower = phase_query.lower()

    for line in lines:
        if PHASE_HEADER_RE.match(line):
            in_phase = phase_lower in line.lower()
            continue
        if SECTION_RE.match(line):
            if in_phase:
                break
            continue
        if in_phase:
            m = TASK_RE.match(line)
            if m:
                tasks.append((m.group(1) == "x", m.group(2)))

    return tasks


def main(plan_file: Path = Path("docs/plan.md")) -> None:
    if len(sys.argv) != 2:
        print("Usage: get_phase_tasks.py <phase-name-or-number>", file=sys.stderr)
        sys.exit(1)
    phase = sys.argv[1]
    text = plan_file.read_text()
    tasks = get_tasks(text, phase)
    if not tasks:
        print(f"No tasks found for phase: {phase}", file=sys.stderr)
        sys.exit(1)
    print(f"\nTasks for phase '{phase}':")
    for completed, description in tasks:
        status = "✓" if completed else "○"
        print(f"  {status} {description}")


if __name__ == "__main__":
    main()
