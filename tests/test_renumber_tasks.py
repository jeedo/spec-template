from template.scripts.renumber_tasks import renumber

SAMPLE = """\
## Phase 1: Setup
- [ ] 1. First task
- [ ] 3. Second task
- [x] 5. Third task done

## Phase 2: Core
- [ ] 10. Fourth task
"""


def test_renumber_sequential() -> None:
    result, count = renumber(SAMPLE)
    assert "- [ ] 1. First task" in result
    assert "- [ ] 2. Second task" in result
    assert "- [x] 3. Third task done" in result
    assert "- [ ] 4. Fourth task" in result
    assert count == 4


def test_renumber_preserves_headers() -> None:
    result, _ = renumber(SAMPLE)
    assert "## Phase 1: Setup" in result
    assert "## Phase 2: Core" in result


def test_renumber_preserves_completed_state() -> None:
    result, _ = renumber(SAMPLE)
    assert "- [x] 3. Third task done" in result


def test_renumber_no_tasks() -> None:
    text = "# Just headers\nNo tasks here\n"
    result, count = renumber(text)
    assert result == text
    assert count == 0


def test_renumber_idempotent() -> None:
    first, _ = renumber(SAMPLE)
    second, count = renumber(first)
    assert first == second
    assert count == 4
