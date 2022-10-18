"""
Test case for Excel blend sequence.
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
from hamcrest import assert_that, equal_to, close_to
from edv_dwh_connector.blend_proposal.excel.blend_proposal_start_cell \
    import BlendProposalStartCell
from edv_dwh_connector.blend_proposal.excel.blend_sequence_start_cell \
    import BlendSequenceStartCell
from edv_dwh_connector.blend_proposal.excel.excel_blend_sequence \
    import ExcelBlendSequence


def test_gets_a_sequence() -> None:
    """
    Tests that it gets a sequence.
    """

    sheet = openpyxl.load_workbook(
        "tests/resources/"
        "3.Daily_Blend_Template_Process_.September_2022.xlsx"
    ).active
    start = BlendSequenceStartCell(
        sheet=sheet,
        bp_start_cell=BlendProposalStartCell(
            sheet=sheet, day=date(2022, 9, 2)
        ),
        number=3
    )
    sequence = ExcelBlendSequence(sheet=sheet, bs_start_cell=start)
    assert_that(
        sequence.name(),
        equal_to("WHEN SURGE_BIN_FR_LG_HG  IS FINISHED"),
        "Sequence name should match"
    )
    assert_that(
        sequence.average_grade(),
        close_to(1.93, 0.01),
        "Sequence average grade should match"
    )
    assert_that(
        sequence.soluble_copper(),
        close_to(159, 0.15),
        "Sequence soluble copper should match"
    )
    assert_that(
        sequence.as_ppm(),
        close_to(365, 1),
        "Sequence As should match"
    )
    assert_that(
        sequence.moisture_estimated(),
        close_to(0.17, 0.007),
        "Sequence moisture estimated should match"
    )
    assert_that(
        sequence.oxide_transition(),
        equal_to(0.7),
        "Sequence oxide/transition should match"
    )
    assert_that(
        sequence.fresh(),
        close_to(0.3, 0.001),
        "Sequence fresh should match"
    )
    assert_that(
        sequence.recovery_blend_estimated(),
        close_to(0.87, 0.007),
        "Sequence recovery blend estimated should match"
    )
    assert_that(
        len(sequence.materials()),
        equal_to(1),
        "Sequence material count should match"
    )
