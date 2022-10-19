# pylint: disable=W0104, E1120, C0103
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
Example Workflows
"""
from sdm.core.workflows import ThreadWF, wf_decorator
from sdm.examples.operators import Hello

workflow = wf_decorator(wf_class=ThreadWF)

@workflow
def HelloWF(head, out):
    """
    Say hello to anyone
    """
    hello = Hello()
    
    head >> hello >> out
