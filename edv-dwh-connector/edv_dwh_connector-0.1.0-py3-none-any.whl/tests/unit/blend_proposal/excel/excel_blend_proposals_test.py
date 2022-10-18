"""
Test case for ExcelBlendProposals.
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
from hamcrest import assert_that, equal_to
from edv_dwh_connector.blend_proposal.excel.excel_blend_proposals \
    import ExcelBlendProposals


def test_gets_blends() -> None:
    """
    Tests that it gets blends.
    """

    blends = ExcelBlendProposals(
        file="tests/resources/"
        "3.Daily_Blend_Template_Process_.September_2022.xlsx",
        start_date=date.fromisoformat("2022-08-30"),
        end_date=date.fromisoformat("2022-09-02")
    )
    assert_that(
        len(blends.items()),
        equal_to(3),
        "Blend proposal items count should match"
    )
