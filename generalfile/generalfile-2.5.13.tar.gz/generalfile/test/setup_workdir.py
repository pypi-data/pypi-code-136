

def setup_workdir():
    """ Set working dir for tests and clear it after it's made sure it's correct path."""
    repo_path = Path().get_parent_repo()

    if not repo_path:
        raise EnvironmentError(f"Failed setting correct woroking dir, current working dir is not inside a repo")

    path = repo_path / repo_path.name() / "test/tests"
    path.set_working_dir()

    if not Path.get_working_dir().endswith("test/tests"):
        raise EnvironmentError(f"Failed setting correct working dir, should be ..test/tests but it's {path}")

    path.delete_folder_content()

from generalfile.path import Path
