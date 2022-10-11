# A component of the BASEmesh pre-processing toolkit.
# Copyright (C) 2020  ETH Zürich
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Custom exceptions for BASEmesh."""


class TopologyError(Exception):
    """Raised for topology violations."""


class TokenError(Exception):
    """Exception raised for token mismatches.

    This is raised when a given opening token is not matched, or if a
    closing token is encountered without a matchign opening token.
    """


class BasemeshWarning(UserWarning):
    """Warning raised for BASEmesh issues.

    These are forwarded to the QGIS GUI for the BASEmesh plugin.
    """
