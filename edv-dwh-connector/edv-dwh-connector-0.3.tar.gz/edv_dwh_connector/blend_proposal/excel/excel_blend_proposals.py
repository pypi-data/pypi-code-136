"""
This module defines list of blend proposals from an Excel file.
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

from datetime import timedelta, date
import openpyxl  # type: ignore
from edv_dwh_connector.blend_proposal.blend_proposals import BlendProposals
from edv_dwh_connector.blend_proposal.excel.excel_blend_proposal \
    import ExcelBlendProposal
from edv_dwh_connector.blend_proposal.excel.blend_proposal_start_cell \
    import BlendProposalStartCell


# pylint: disable=too-few-public-methods
class ExcelBlendProposals(BlendProposals):
    """
    Blend proposals from Excel file.
    """

    def __init__(self, file: str, start_date: date, end_date: date):
        """
        Ctor.
        :param file: Path of Excel file
        :param start_date: Start date
        :param end_date: End date
        """
        self.__file = file
        self.__start_date = start_date
        self.__end_date = end_date

    def items(self) -> list:
        arrays = []
        book = openpyxl.load_workbook(self.__file)
        delta = self.__end_date - self.__start_date
        for day in range(0, delta.days):
            bps = BlendProposalStartCell(
                sheet=book.active, day=self.__start_date + timedelta(days=day)
            )
            if bps.exist():
                arrays.append(
                    ExcelBlendProposal(sheet=book.active, bp_start_cell=bps)
                )
        return arrays
