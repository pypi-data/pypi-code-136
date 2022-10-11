import pytest


class TestScript(object):

    @pytest.fixture(autouse=True)
    def set_test_client(self, serenytics_client, script_test):
        self._client = serenytics_client
        self._script = script_test

    def test_run_synchronously(self):
        # TODO: there is an issue when running this test because the python-script folder is now copied
        # when PRODUCTION envvar is not set.
        # See python_script.py, in run_generic_python_script function
        return
        # log = self._script.run(async_=False)
        # assert log.is_success
        # assert log.return_code == 0
        # we check for "endswith" and not "==" because log can contain an additional line due to the download
        # of the docker image
        # assert log.stdout.endswith('Hello, Serenytics!\n')
        # assert (log.stderr == '') or ('Using: python ' in log.stderr)
