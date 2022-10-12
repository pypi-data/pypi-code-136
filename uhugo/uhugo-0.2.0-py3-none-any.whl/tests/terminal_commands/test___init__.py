from uhugo.terminal_commands import hugo_version_cmd


def test_hugo_version_cmd(fake_process):
    fake_process.register_subprocess(["hugo", "version"], stdout="hugo v0.85.0-724D5DB5+extended darwin/amd64 BuildDate=2021-07-05T10:46:28Z VendorInfo=gohugoio")

    data = hugo_version_cmd()
    assert data == b"hugo v0.85.0-724D5DB5+extended darwin/amd64 BuildDate=2021-07-05T10:46:28Z VendorInfo=gohugoio"
