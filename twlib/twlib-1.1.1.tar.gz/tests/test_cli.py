import pytest
from typer.testing import CliRunner

from twlib.environment import ROOT_DIR
from twlib.git_open import app
from twlib.main import app as twlib

runner = CliRunner()


# noinspection PyPep8Naming
class TestConverter:
    def test_convert_heif(self):
        INPUT_FILE = ROOT_DIR / "tests" / "resources" / "input.heic"
        result = runner.invoke(twlib, ["convert-heif", str(INPUT_FILE)])
        print(result.stdout)
        assert result.exit_code == 0


class TestGitOpen:
    @pytest.mark.parametrize(
        ("path", "url"),
        ((".", "https://github.com/sysid/twlib"),),
    )
    def test_git_open(self, mocker, path, url):
        mocked = mocker.patch("twlib.git_open.webbrowser.open")
        result = runner.invoke(app, path)
        print(result.stdout)
        assert result.exit_code == 0
        assert url in result.stdout


class TestEpochConvert:
    @pytest.mark.parametrize(
        ("epoch", "dt", "is_local"),
        (
            ("1347517370", "2012-09-13 06:22:50\n", False),  # epoch must be str ???
            ("1347517370", "2012-09-13 08:22:50\n", True),
        ),
    )
    def test_epoch2dt(self, epoch, dt, is_local):
        # result = runner.invoke(app, ["epoch2datetime", epoch, "-v"], input="y\n")
        if is_local:
            result = runner.invoke(twlib, ["epoch2dt", epoch, "--to-local"])
        else:
            result = runner.invoke(twlib, ["epoch2dt", epoch])
        print(result.stdout)
        assert result.exit_code == 0
        assert result.stdout == dt

    @pytest.mark.parametrize(
        ("dt", "epoch", "is_local"),
        (
            # ("2012-09-13 06:22:50", "1347517370.0\n", False),  # epoch must be str ???
            ("2012-09-13 08:22:50", "1347517370.0\n", True),  # epoch must be str ???
        ),
    )
    def test_dt2epoch(self, dt, epoch, is_local):
        # result = runner.invoke(app, ["epoch2datetime", epoch, "-v"], input="y\n")
        if is_local:
            result = runner.invoke(twlib, ["dt2epoch", dt, "--is-local"])
        else:
            result = runner.invoke(twlib, ["dt2epoch", dt])
        print(result.stdout)
        assert result.exit_code == 0
        assert result.stdout == epoch
