"""
Test case for BlendProposalStartCell.
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

from datetime import date
import openpyxl  # type: ignore
from hamcrest import assert_that, is_, equal_to
from edv_dwh_connector.blend_proposal.excel.blend_proposal_start_cell \
    import BlendProposalStartCell


sheet = openpyxl.load_workbook(
    "tests/resources/"
    "3.Daily_Blend_Template_Process_.September_2022.xlsx"
).active


def test_finds_start_cell() -> None:
    """
    Tests that it finds a cell position.
    """
    blend = BlendProposalStartCell(sheet=sheet, day=date(2022, 9, 1))
    assert_that(
        blend.exist(), is_(True),
        "Blend should exist"
    )
    assert_that(
        blend.row(), equal_to(7),
        "Blend start cell row should match"
    )
    assert_that(
        blend.column(), equal_to(972),
        "Blend start cell column should match"
    )


def test_finds_not_start_cell() -> None:
    """
    Tests that it doesn't find non-existent cell.
    """
    blend = BlendProposalStartCell(sheet=sheet, day=date(2022, 6, 1))
    assert_that(blend.exist(), is_(False))
