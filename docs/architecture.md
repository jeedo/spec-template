# Architecture: spec-template

> **Status**: Approved
> **Last Updated**: 2026-05-10

## Overview & Goals

spec-template is a GitHub template repository that gives Claude a consistent, repeatable starting point for spec-driven development. The goal is to eliminate the repetitive setup instructions a developer must give Claude at the start of every project by shipping a `CLAUDE.md`, documentation templates, and task management scripts as first-class project artifacts.

**Success Criteria**:
- A developer can create a new repo from this template and Claude immediately understands the workflow without extra prompting
- Tasks in `plan.md` are always sequentially numbered and checkboxes stay in sync with implementation progress
- The red-green TDD cycle is enforced by Claude's instructions, not by build tooling alone

## Tech Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Script language | Python 3.11+ | Cross-platform, stdlib-only scripts require no install |
| Package manager | uv | Fast, modern Python tooling; lockfile support |
| Linting + format | ruff | Single tool replacing black, isort, flake8 |
| Type checking | mypy (strict) | Catches bugs early in utility scripts |
| Testing | pytest | Flexible, widely supported |
| CI | GitHub Actions | Native GitHub integration, free for public repos |

## System Components

### CLAUDE.md
The primary artifact of this template. Contains all workflow instructions Claude reads at session start: architecture-first approach, TDD enforcement, branching conventions, conventional commit format, uv rules, and script usage.

### docs/
- `architecture.md` — high-level system design, filled in collaboratively with the user before any code is written
- `plan.md` — phased, sequentially numbered, checkboxed task list derived from the architecture document

### scripts/
Python utilities Claude uses to maintain `docs/plan.md` integrity:
- `renumber_tasks.py` — restores sequential numbering after tasks are added or removed
- `complete_task.py` — marks a specific task done by its number
- `get_phase_tasks.py` — prints all tasks (and their completion status) for a named or numbered phase

### .github/workflows/ci.yml
Runs ruff lint, ruff format check, mypy type checking, and pytest on every push and pull request to `main`.

## Data Model / API

### plan.md task format
```
- [ ] <number>. <description>   # incomplete task
- [x] <number>. <description>   # completed task
```
Tasks are grouped under `## Phase N: <Name>` section headers. Numbers are unique and sequential across all phases.

### Script interface
All scripts read from `docs/plan.md` relative to the working directory and are invoked as:
```bash
python scripts/renumber_tasks.py
python scripts/complete_task.py <task-number>
python scripts/get_phase_tasks.py <phase-name-or-number>
```

## Research & References

No additional research performed for this project.
