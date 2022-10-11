from pathlib import Path

import pytest

from twlib.link_vimwiki import Link, extract_link_data, transform_link


@pytest.mark.parametrize(
    ("line", "link", "target"),
    (
        (
            "123278618        0 lrwxr-xr-x    1 Q187392          staff                  19 Feb 23 18:13 /Users/Q187392/vimwiki//proj/csf.md -> meldelinie_laden.md",
            "/Users/Q187392/vimwiki/proj/csf.md",
            "meldelinie_laden.md",
        ),
        (
            "130629669        0 lrwxr-xr-x    1 Q187392          staff                  55 May 29 12:48 /Users/Q187392/vimwiki//dev/algo/.venv/bin/python -> /Users/Q187392/.asdf/installs/python/3.10.4/bin/python3",
            "/Users/Q187392/vimwiki//dev/algo/.venv/bin/python",
            "/Users/Q187392/.asdf/installs/python/3.10.4/bin/python3",
        ),
        (
            "96714484        0 lrwxr-xr-x    1 Q187392          staff                  23 Sep  9  2021 /Users/Q187392/vimwiki//binx -> /Users/Q187392/dev/binx",
            "/Users/Q187392/vimwiki//binx",
            "/Users/Q187392/dev/binx",
        ),
    ),
)
def test_extract_link_data(line, link, target):
    print(line)
    l = extract_link_data(line)
    assert l.link == Path(link)
    assert l.target == Path(target)


# @pytest.mark.skip("Fragile tests due to Path.home() usage")
@pytest.mark.parametrize(
    ("link_obj", "link", "target"),
    (
        (
            Link(Path("/Users/Q187392/vimwiki//binx"), Path("/Users/Q187392/dev/binx")),
            "/Users/tw/vimwiki//binx",
            "/Users/tw/dev/binx",
        ),
        (
            Link(
                Path("/Users/Q187392/vimwiki/proj/csf.md"), Path("meldelinie_laden.md")
            ),
            "/Users/tw/vimwiki/proj/csf.md",
            "/Users/tw/vimwiki/proj/meldelinie_laden.md",
        ),
    ),
)
def test_transform_link(mocker, link_obj, link, target):
    mocker.patch(
        "twlib.link_vimwiki.SOURCE_VIMWIKI_PATH", Path("/Users/Q187392/vimwiki")
    )
    mocker.patch("twlib.link_vimwiki.DEST_VIMWIKI_PATH", Path("/Users/tw/vimwiki"))
    mocker.patch("twlib.link_vimwiki.SOURCE_HOME", Path("/Users/Q187392"))
    mocker.patch("twlib.link_vimwiki.DEST_HOME", Path("/Users/tw"))
    mocker.patch("twlib.link_vimwiki.Path.home", return_value=Path("/Users/tw"))
    # mocker.patch("twlib.link_vimwiki.transform_link", return_value=Link(Path(link), Path(target)))
    l = transform_link(link_obj)
    assert l.link == Path(link)
    assert l.target == Path(target)
