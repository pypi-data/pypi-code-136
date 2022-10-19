"""
This module defines Blend sequence start cell.
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

import re
from openpyxl.worksheet.worksheet import Worksheet   # type: ignore
from edv_dwh_connector.blend_proposal.excel.start_cell import StartCell


class BlendSequenceStartCell(StartCell):
    """
    Start cell of a blend sequence.
    .. since: 0.1
    """

    def __init__(
        self, sheet: Worksheet, bp_start_cell: StartCell, number: int
    ) -> None:
        """
        Ctor.
        :param sheet: Sheet
        :param bp_start_cell: Blend proposal start cell
        :param number: Sequence number
        :raises ValueError: If wrong number or cell doesn't exist
        """

        super().__init__()
        if number < 1 or number > 5:
            raise ValueError("Sequence number should be between 1 and 5")
        if not bp_start_cell.exist():
            raise ValueError("Daily blend proposal not found")
        self.__sheet = sheet
        self.__bp_start_cell = bp_start_cell
        self.__number = number

    def _find(self) -> tuple:
        frow, fcolumn = -1, -1
        rrow, rcol = self.__bp_start_cell.row(), \
            self.__bp_start_cell.column()
        curnum = 0
        for row in range(rrow, rrow + 500):
            current = self.__sheet.cell(row, rcol)
            if current.value is not None and re.search(
                "sequence", current.value, re.IGNORECASE
            ):
                curnum = curnum + 1
                if curnum == self.__number:
                    frow, fcolumn = row, rcol
                    break
        return frow, fcolumn
