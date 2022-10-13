from requirements_extractor.gitlab_models import _find_requirement_part, GitlabIssue, References


def test_find_requirements_to_end():
    description = 'We do not cover all issues, only those with labels or scoped labels\n\n## Requirements\n' \
                  '- support label-list with simple labels\n- support label-list with scoped labels\n' \
                  '- support scoped label group with `label::` without details\n- all labels are treated euqally (OR)'
    result = _find_requirement_part(description)
    assert isinstance(result, tuple)
    assert result == (84, 262)


def test_find_acceptance_start():
    description = '## Acceptance criteria\n-criteria 1\n### sub-headline\n## Next chapter'
    result = _find_requirement_part(description)
    assert result == (22, 51)


def test_find_acceptance_middle():
    description = '# a headline\n## another headline\n some acceptance criteria or requiremnts may be here\n' \
                  '## Acceptance criteria\n-criteria 1\n### sub-headline\n## Next chapter'
    result = _find_requirement_part(description)
    assert result == (108, 137)


def test_get_acs():
    description = '# a headline\n## another headline\n some acceptance criteria or requiremnts may be here\n' \
                  '## Acceptance criteria\n-criteria 1\n### sub-headline\n## Next chapter'
    gi = GitlabIssue(id=1, iid=1, title="x", state="x", labels=[], references=References(short="", full=""),
                     description=description)
    result = gi.get_requirements()
    assert result == ['criteria 1']  # ignore sub-headline completely


def test_find_nix():
    description = 'Some none Acceptance criteria\n-criteria 1\n### sub-headline\n## Next chapter'
    result = _find_requirement_part(description)
    assert result == (0, 0)
