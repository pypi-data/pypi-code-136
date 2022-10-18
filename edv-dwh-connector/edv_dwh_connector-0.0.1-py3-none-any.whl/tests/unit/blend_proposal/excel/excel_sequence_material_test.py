"""
Test case for ExcelSequenceMaterial.
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
from edv_dwh_connector.blend_proposal.excel.excel_sequence_material \
    import ExcelSequenceMaterial
from edv_dwh_connector.blend_proposal.excel.sequence_material_start_cell \
    import SequenceMaterialStartCell


sheet = openpyxl.load_workbook(
    "tests/resources/"
    "3.Daily_Blend_Template_Process_.September_2022.xlsx"
).active


def test_gets_a_material_with_pit() -> None:
    """
    Tests that it gets a material with pit.
    """
    bs_start = BlendSequenceStartCell(
        sheet=sheet,
        bp_start_cell=BlendProposalStartCell(
            sheet=sheet, day=date(2022, 8, 21)
        ),
        number=1
    )
    sm_start = SequenceMaterialStartCell(row=17, column=899)
    material = ExcelSequenceMaterial(
        sheet=sheet, bs_start_cell=bs_start, sm_start_cell=sm_start
    )
    assert_that(
        material.name(),
        equal_to("SURGE_BIN_FR_LG_HG"),
        "Material name should match"
    )
    assert_that(
        material.machine_type(),
        equal_to("SURGE BIN"),
        "Material type should match"
    )
    assert_that(
        material.pit(),
        equal_to("WAL / LEP / BAK"),
        "Material pit should match"
    )
    assert_that(
        material.au_grade(),
        equal_to(1.48),
        "Material Au grade should match"
    )
    assert_that(
        material.sol_cu(),
        close_to(473, 0.9),
        "Material sol cu should match"
    )
    assert_that(
        material.as_ppm(),
        equal_to(93),
        "Material As should match"
    )
    assert_that(
        material.moisture(),
        equal_to(0.12),
        "Material Moisture should match"
    )
    assert_that(
        material.indicative_rec(),
        equal_to(0.88),
        "Material Indicative rec should match"
    )
    assert_that(
        material.bucket(),
        equal_to(1),
        "Material Bucket should match"
    )
    assert_that(
        material.available_tons(),
        equal_to(1500),
        "Material Available tons should match"
    )
    assert_that(
        material.prop(),
        close_to(0.16, 0.007),
        "Material Prop should match"
    )


def test_gets_a_material_without_pit() -> None:
    """
    Tests that it gets a material without pit.
    """
    bs_start = BlendSequenceStartCell(
        sheet=sheet,
        bp_start_cell=BlendProposalStartCell(
            sheet=sheet, day=date(2022, 7, 21)
        ),
        number=1
    )
    sm_start = SequenceMaterialStartCell(row=15, column=452)
    material = ExcelSequenceMaterial(
        sheet=sheet, bs_start_cell=bs_start, sm_start_cell=sm_start
    )
    assert_that(
        material.name(),
        equal_to("DPL_LG_HG_AS"),
        "Material name without pit should match"
    )
    assert_that(
        material.machine_type(),
        equal_to("CRUSHER"),
        "Material type without pit should match"
    )
    assert_that(
        material.pit(),
        equal_to(""),
        "Material pit without pit should match"
    )
