# Implementation Plan

> Generated from [Architecture](architecture.md)
> **Last Updated**: 2026-05-10

## Phase 1: Setup & Scaffolding

- [ ] 1. Create `pyproject.toml` with uv, ruff, mypy, and pytest configured
- [ ] 2. Create `.gitignore`
- [ ] 3. Create `scripts/__init__.py` and `tests/__init__.py`

## Phase 2: Documentation

- [ ] 4. Create `CLAUDE.md` with full workflow instructions
- [ ] 5. Fill in `docs/architecture.md` for the template project itself

## Phase 3: Task Management Scripts

- [ ] 6. Write failing tests for `renumber_tasks` (red)
- [ ] 7. Implement `scripts/renumber_tasks.py` until tests pass (green)
- [ ] 8. Write failing tests for `complete_task` (red)
- [ ] 9. Implement `scripts/complete_task.py` until tests pass (green)
- [ ] 10. Write failing tests for `get_phase_tasks` (red)
- [ ] 11. Implement `scripts/get_phase_tasks.py` until tests pass (green)

## Phase 4: CI/CD

- [ ] 12. Create `.github/workflows/ci.yml` with lint, type check, and test jobs
- [ ] 13. Verify all checks pass locally with `uv run pytest` and `uv run ruff check .`
