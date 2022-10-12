from packaging import version

from uhugo.terminal_commands import Hugo
from uhugo.terminal_commands.posix import check_hugo


def test_check_hugo(fake_process):
    fake_process.register_subprocess(["command", "-v", "hugo"], stdout=Hugo("", False, version.Version("0")))

    data = check_hugo()
    assert data == Hugo("", False, version.Version("0"))
