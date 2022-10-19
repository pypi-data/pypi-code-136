import os
import shutil
import tempfile
from unittest.mock import patch
from zipfile import ZipFile

from anyscale import snapshot_util


class TestWorkspaceEnv:
    def __init__(self):
        self.tmpdir = tempfile.mkdtemp()
        self.workspace_dir = os.path.join(self.tmpdir, "work")
        os.makedirs(self.workspace_dir)
        self.efs_dir = os.path.join(self.tmpdir, "efs")
        os.makedirs(self.efs_dir)

        # Rewire snapshot_util to use our test env setup.
        snapshot_util.WORKING_DIR = self.workspace_dir
        snapshot_util.EFS_WORKSPACE_DIR = os.path.join(self.efs_dir, "workspaces")
        snapshot_util.WORKSPACE_ID = "test_ws1"
        # TODO: flesh this out.

    def __del__(self):
        shutil.rmtree(self.tmpdir)


def list_zip(zipfile):
    with ZipFile(zipfile, "r") as z:
        return z.namelist()


def test_snapshot_on_change():
    env = TestWorkspaceEnv()
    os.chdir(env.workspace_dir)

    # Generate a test workspace with a single file.
    with open("foo.txt", "w"):
        pass

    # Create a snapshot.
    assert not snapshot_util.find_latest(True)
    snapshot_util.do_snapshot()
    s1 = snapshot_util.find_latest(True)
    assert s1 is not None, s1

    # No change.
    snapshot_util.do_snapshot()
    s2 = snapshot_util.find_latest(True)
    assert s1 == s2, (s1, s2)

    # Generate a test workspace with a single file.
    with open("foo.txt", "w") as f:
        f.write("changed!")

    # Change.
    snapshot_util.do_snapshot()
    s3 = snapshot_util.find_latest(True)
    assert s2 != s3, (s2, s3)


@patch("os.path.ismount")
def test_env_hook_doesnt_delete_snapshots(mock_is_mount):
    env = TestWorkspaceEnv()
    os.chdir(env.workspace_dir)

    # Generate a test workspace with a single file.
    with open("foo.txt", "w"):
        pass

    # Sanity check.
    r = snapshot_util.env_hook({})
    assert r == {"working_dir": "/tmp/ray_latest_runtime_env.zip"}

    # Create a snapshot.
    assert not snapshot_util.find_latest(True)
    snapshot_util.do_snapshot()
    s1 = snapshot_util.find_latest(True)
    assert s1 is not None, s1

    # Snapshot shouldn't be deleted or otherwise affected by env hook.
    r = snapshot_util.env_hook({})
    assert r == {"working_dir": "/tmp/ray_latest_runtime_env.zip"}
    s2 = snapshot_util.find_latest(True)
    assert s1 == s2, (s1, s2)


@patch("os.path.ismount")
def test_env_hook_rel_mode(mock_is_mount):
    env = TestWorkspaceEnv()
    os.chdir(env.workspace_dir)

    os.makedirs("subdir")
    os.chdir("subdir")
    with open("foo.txt", "w"):
        pass

    # Test absolute mode.
    snapshot_util.RELATIVE_WORKING_DIR = False
    r = snapshot_util.env_hook({})
    assert r == {"working_dir": "/tmp/ray_latest_runtime_env.zip"}
    assert list_zip("/tmp/ray_latest_runtime_env.zip") == ["subdir/", "subdir/foo.txt"]

    # Test relative mode.
    snapshot_util.RELATIVE_WORKING_DIR = True
    r = snapshot_util.env_hook({})
    assert r == {"working_dir": "/tmp/ray_latest_runtime_env.zip"}
    assert list_zip("/tmp/ray_latest_runtime_env.zip") == ["foo.txt"]
