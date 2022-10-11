import pytest

from twlib.git_open import extract_url, get_git_url


@pytest.mark.parametrize(
    ("url", "result"),
    (
        (
            "ssh://git@git.energyservices.cloud:2222/energy-services/powerpool-v3/powerpool.git",
            "https://git.energyservices.cloud/energy-services/powerpool-v3/powerpool.git",
        ),
        (
            "git@git.energyservices.cloud:2222/energy-services/powerpool-v3/powerpool.git",
            "https://git.energyservices.cloud/energy-services/powerpool-v3/powerpool.git",
        ),
        (
            "https://github.com/sysid/vimania.git",
            "https://github.com/sysid/vimania.git",
        ),
    ),
)
def test_extract_url(url, result):
    assert extract_url(url) == result


@pytest.mark.skip("Integration Test: only runs with updated BMW setup")
@pytest.mark.parametrize(
    ("path", "url"),
    (
        (
            "/Users/Q187392/dev/x/ENERGY-SERVICES/powerpool-v3/powerpool/service/simulation",
            "git-e4m-prod.bmwgroup.net/energy-services/powerpool-v3/powerpool.git",
        ),
        ("/Users/Q187392/dev/vim/vimania", "https://github.com/sysid/vimania.git"),
    ),
)
def test_get_git_url(path, url):
    assert url in get_git_url(path)
