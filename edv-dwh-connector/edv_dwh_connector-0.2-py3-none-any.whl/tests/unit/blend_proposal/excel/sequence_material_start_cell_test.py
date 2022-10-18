"""
Test case for SequenceMaterialStartCell.
.. since: 0.1
"""

# -*- coding: utf-8 -*-
# Copyright (c) 2022 Endeavour Mining
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to read
# the Software only. Permissions is hereby NOT GRANTED to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from hamcrest import assert_that, is_, equal_to
from edv_dwh_connector.blend_proposal.excel.sequence_material_start_cell \
    import SequenceMaterialStartCell


def test_finds_start_cell() -> None:
    """
    Tests it finds a cell position.
    """
    stc = SequenceMaterialStartCell(row=5, column=7)
    assert_that(
        stc.exist(), is_(True),
        "Material should exist"
    )
    assert_that(
        stc.row(), equal_to(5),
        "Material start cell row should match"
    )
    assert_that(
        stc.column(), equal_to(7),
        "Material start cell column should match"
    )
