from template.scripts.complete_task import complete

SAMPLE = """\
## Phase 1
- [ ] 1. First task
- [ ] 2. Second task
- [x] 3. Already done
"""


def test_complete_marks_checkbox() -> None:
    result, found = complete(SAMPLE, 1)
    assert found
    assert "- [x] 1. First task" in result


def test_complete_preserves_other_tasks() -> None:
    result, _ = complete(SAMPLE, 1)
    assert "- [ ] 2. Second task" in result


def test_complete_preserves_already_done() -> None:
    result, _ = complete(SAMPLE, 1)
    assert "- [x] 3. Already done" in result


def test_complete_not_found_returns_false() -> None:
    _, found = complete(SAMPLE, 99)
    assert not found


def test_complete_already_done_not_matched() -> None:
    # [x] tasks don't match the incomplete pattern, so found == False
    _, found = complete(SAMPLE, 3)
    assert not found


def test_complete_text_unchanged_when_not_found() -> None:
    result, _ = complete(SAMPLE, 99)
    assert result == SAMPLE
