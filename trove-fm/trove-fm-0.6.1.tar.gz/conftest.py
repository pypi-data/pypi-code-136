
"""
TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""


import pytest


##########################
##### Custom Options #####
##########################


# ! IMPORTANT: This function should be implemented only in plugins or conftest.py files situated
# ! at the tests root directory due to how pytest discovers plugins during startup.


def pytest_addoption(parser):
    parser.addoption(
        "--save-state",
        action="store_true",
        default=False,
        help="preserve the state of the database at the conclusion of the test."
    )


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if config.getoption("--save-state"):
        message = 'The database was NOT cleaned up after this test run!!!'
        terminalreporter.ensure_newline()
        terminalreporter.section('State Saved', sep='-', blue=True, bold=True)
        terminalreporter.line(message)


@pytest.fixture(scope="session")
def save_state(request):
    return request.config.getoption("--save-state")
