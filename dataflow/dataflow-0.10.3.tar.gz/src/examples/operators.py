# pylint: disable=C0103
# Copyright (C) 2021 ALBA Synchrotron
#
# This file is part SDM Core
#
# SDM Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SDM Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SDM Core.  If not, see <http://www.gnu.org/licenses/>.

"""
Example Operators
"""

from sdm.core.operators import BasicOP, op_decorator
from sdm.core.workflows import DONE

operator = op_decorator(BasicOP)


@operator
def Hello(item, task):
    """
    Say Hello
    """
    
    if item is DONE:
        return

    person = item
    message = f"Hello {person}"
    print(message)
    return message
