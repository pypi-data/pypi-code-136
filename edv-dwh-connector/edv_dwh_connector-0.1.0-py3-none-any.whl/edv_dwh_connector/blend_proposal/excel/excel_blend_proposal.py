"""
This module defines Excel blend proposal.
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
from openpyxl.worksheet.worksheet import Worksheet  # type: ignore
from edv_dwh_connector.blend_proposal.blend_proposal import BlendProposal
from edv_dwh_connector.blend_proposal.excel.excel_blend_sequence \
    import ExcelBlendSequence
from edv_dwh_connector.blend_proposal.excel.blend_sequence_start_cell \
    import BlendSequenceStartCell
from edv_dwh_connector.blend_proposal.excel.start_cell \
    import StartCell


class ExcelBlendProposal(BlendProposal):
    """
    Excel blend proposal.
    .. since: 0.1
    """

    def __init__(self, sheet: Worksheet, bp_start_cell: StartCell) -> None:
        """
        Ctor.
        :param sheet: Worksheet
        :param bp_start_cell: Blend proposal start cell
        """
        self.__sheet = sheet
        self.__bp_start_cell = bp_start_cell

    def date(self) -> date:
        return self.__sheet.cell(
            self.__bp_start_cell.row(), self.__bp_start_cell.column() + 1
        ).value.date()

    def sequences(self) -> list:
        items = []
        for number in range(1, 5):
            try:
                scell = BlendSequenceStartCell(
                    self.__sheet, self.__bp_start_cell, number
                )
                if scell.exist():
                    items.append(
                        ExcelBlendSequence(self.__sheet, scell)
                    )
            except ValueError:
                break
        return items
