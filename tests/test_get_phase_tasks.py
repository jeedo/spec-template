from scripts.get_phase_tasks import get_tasks

SAMPLE = """\
## Phase 1: Setup
- [ ] 1. Init repo
- [x] 2. Configure linting

## Phase 2: Core
- [ ] 3. Implement logic
- [ ] 4. Write tests
"""


def test_get_tasks_by_number() -> None:
    tasks = get_tasks(SAMPLE, "1")
    assert len(tasks) == 2
    assert tasks[0] == (False, "1. Init repo")
    assert tasks[1] == (True, "2. Configure linting")


def test_get_tasks_by_name() -> None:
    tasks = get_tasks(SAMPLE, "Core")
    assert len(tasks) == 2
    assert tasks[0] == (False, "3. Implement logic")


def test_get_tasks_case_insensitive() -> None:
    tasks = get_tasks(SAMPLE, "setup")
    assert len(tasks) == 2


def test_get_tasks_completed_flag() -> None:
    tasks = get_tasks(SAMPLE, "1")
    assert tasks[0][0] is False
    assert tasks[1][0] is True


def test_get_tasks_phase_not_found() -> None:
    tasks = get_tasks(SAMPLE, "nonexistent")
    assert tasks == []
