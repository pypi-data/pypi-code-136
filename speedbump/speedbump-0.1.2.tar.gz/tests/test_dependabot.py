from pytest_shell.fs import create_files
from pytest_shell.shell import LocalBashSession


def test_empty_repo(bash: LocalBashSession, tmpdir):
    with bash(pwd=str(tmpdir)) as s:
        s.run_script("git", args=["init"])
        s.run_script("speedbump")
        assert not s.path_exists(".github/dependabot.yml")


def test_github_actions(bash: LocalBashSession, tmpdir):
    create_files(
        structure=[
            {".github/workflows/example.yml": {"content": "DUMMY"}},
        ],
        root=tmpdir,
    )

    with bash(pwd=str(tmpdir)) as s:
        s.run_script("git", args=["init"])
        s.run_script("git", args=["add", ".github/workflows/example.yml"])
        assert ".github/workflows/example.yml" in s.run_script(
            "git", args=["ls-files"]
        )

        s.run_script("speedbump")
        assert s.path_exists(f"{tmpdir}/.github/dependabot.yml")
