import tempfile
from pathlib import Path

from uhugo.checks import bin_folder, get_latest_version_api


def test_bin_folder(monkeypatch):

    with tempfile.TemporaryDirectory() as tdir:

        def mockreturn():
            return Path(tdir)

        monkeypatch.setattr(Path, 'home', mockreturn)
        bin_dir = bin_folder()

        assert bin_dir == Path(tdir, 'bin').__str__()


def test_get_latest_version_api(requests_mock):
    requests_mock.get("https://api.github.com/repos/gohugoio/hugo/releases/latest", json={'tag_name': 'v0.85.0'})
    assert '0.85.0' == get_latest_version_api()


def test_get_latest_version_api_override(requests_mock):
    requests_mock.get("https://api.github.com/repos/gohugoio/hugo/releases/tags/v0.85.0", text='0.85.0')
    assert '0.85.0' == get_latest_version_api('0.85.0')
