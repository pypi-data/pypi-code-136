import pytest

from sila2_interop_communication_tester import __version__
from sila2_interop_communication_tester.helpers.pytest_reporter import NotTruncatingTerminalReporter
from sila2_interop_communication_tester.test_server.helpers.spy import ServerCall

# is set in __main__.py
RPC_CALL_ARGS: dict[str, list[ServerCall]]


@pytest.fixture(scope="session")
def server_calls() -> dict[str, list[ServerCall]]:
    return RPC_CALL_ARGS  # noqa: F821


@pytest.mark.trylast
def pytest_configure(config):
    vanilla_reporter = config.pluginmanager.getplugin("terminalreporter")
    my_reporter = NotTruncatingTerminalReporter(config)
    config.pluginmanager.unregister(vanilla_reporter)
    config.pluginmanager.register(my_reporter, "terminalreporter")


@pytest.fixture(scope="session", autouse=True)
def log_global_env_facts(record_testsuite_property):
    record_testsuite_property("version", __version__)
