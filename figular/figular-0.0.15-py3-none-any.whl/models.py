# SPDX-FileCopyrightText: 2021-2 Galagic Limited, et. al. <https://galagic.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# figular generates visualisations from flexible, reusable parts
#
# For full copyright information see the AUTHORS file at the top-level
# directory of this distribution or at
# [AUTHORS](https://gitlab.com/thegalagic/figular/AUTHORS.md)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, Extra, constr, conint, confloat
from typing import Optional
import re
import string


class OutputFormatEnum(str, Enum):
    svg = 'svg'
    png = 'png'

    def getext(self):
        if self is OutputFormatEnum.svg:
            return 'svg'
        if self is OutputFormatEnum.png:
            return 'png'

    def getmime(self):
        if self is OutputFormatEnum.svg:
            return 'image/svg+xml'
        if self is OutputFormatEnum.png:
            return 'image/png'


class ColorEnum(str, Enum):
    Black = 'Black'
    Cyan = 'Cyan'
    Magenta = 'Magenta'
    Yellow = 'Yellow'
    black = 'black'
    blue = 'blue'
    brown = 'brown'
    chartreuse = 'chartreuse'
    cyan = 'cyan'
    darkblue = 'darkblue'
    darkbrown = 'darkbrown'
    darkcyan = 'darkcyan'
    darkgray = 'darkgray'
    darkgreen = 'darkgreen'
    darkgrey = 'darkgrey'
    darkmagenta = 'darkmagenta'
    darkolive = 'darkolive'
    darkred = 'darkred'
    deepblue = 'deepblue'
    deepcyan = 'deepcyan'
    deepgray = 'deepgray'
    deepgreen = 'deepgreen'
    deepgrey = 'deepgrey'
    deepmagenta = 'deepmagenta'
    deepred = 'deepred'
    deepyellow = 'deepyellow'
    fuchsia = 'fuchsia'
    gray = 'gray'
    green = 'green'
    grey = 'grey'
    heavyblue = 'heavyblue'
    heavycyan = 'heavycyan'
    heavygray = 'heavygray'
    heavygreen = 'heavygreen'
    heavygrey = 'heavygrey'
    heavymagenta = 'heavymagenta'
    heavyred = 'heavyred'
    lightblue = 'lightblue'
    lightcyan = 'lightcyan'
    lightgray = 'lightgray'
    lightgreen = 'lightgreen'
    lightgrey = 'lightgrey'
    lightmagenta = 'lightmagenta'
    lightolive = 'lightolive'
    lightred = 'lightred'
    lightyellow = 'lightyellow'
    magenta = 'magenta'
    mediumblue = 'mediumblue'
    mediumcyan = 'mediumcyan'
    mediumgray = 'mediumgray'
    mediumgreen = 'mediumgreen'
    mediumgrey = 'mediumgrey'
    mediummagenta = 'mediummagenta'
    mediumred = 'mediumred'
    mediumyellow = 'mediumyellow'
    olive = 'olive'
    orange = 'orange'
    paleblue = 'paleblue'
    palecyan = 'palecyan'
    palegray = 'palegray'
    palegreen = 'palegreen'
    palegrey = 'palegrey'
    palemagenta = 'palemagenta'
    palered = 'palered'
    paleyellow = 'paleyellow'
    pink = 'pink'
    purple = 'purple'
    red = 'red'
    royalblue = 'royalblue'
    salmon = 'salmon'
    springgreen = 'springgreen'
    white = 'white'
    yellow = 'yellow'


class BorderStyleEnum(str, Enum):
    solid = 'solid'
    dotted = 'dotted'
    dashed = 'dashed'
    longdashed = 'longdashed'
    dashdotted = 'dashdotted'
    longdashdotted = 'longdashdotted'


class FontEnum(str, Enum):
    avantgarde = 'Avant Garde'
    bookman = 'Bookman'
    computermodern_roman = 'Computer Modern Roman'
    computermodern_sansserif = 'Computer Modern Sans'
    computermodern_teletype = 'Computer Modern Teletype'
    courier = 'Courier'
    dejavu_sansserif = 'DejaVu Sans'
    helvetica = 'Helvetica'
    newcenturyschoolbook = 'New Century Schoolbook'
    palatino = 'Palatino'
    symbol = 'Symbol'
    timesroman = 'Times New Roman'
    zapfchancery = 'Zapf Chancery'
    zapfdingbats = 'Zapf Dingbats'


class FontWeightEnum(str, Enum):
    normal = 'normal'
    bold = 'bold'


def _asystylerule(cleanArgs, index, parentselector, selector):
    finalselector: string = f"selector({selector}"

    if (index):
        finalselector += f", {index})"
    else:
        finalselector += ")"

    if (parentselector != ""):
        finalselector = f"{parentselector}, {finalselector}"

    return (f"dom_styledom.addrule(stylerule(selectorlist({finalselector}), "
            f"style({','.join(cleanArgs)})))")


class Line(BaseModel, extra=Extra.forbid):
    border_color: Optional[ColorEnum]
    border_width: Optional[confloat(ge=0, le=100)]
    border_style: Optional[BorderStyleEnum]

    def getasy(self, parentselector):
        cleanArgs = []
        if self.border_color:
            cleanArgs.append(
                f"border_color={self.border_color}")
        if self.border_width is not None:
            cleanArgs.append(
                f"border_width={self.border_width}")
        if self.border_style:
            cleanArgs.append(
                f"border_style={self.border_style}")
        if cleanArgs:
            return _asystylerule(cleanArgs, None, parentselector,
                                 "elementtype.line")
        return ""


class Shape(BaseModel, extra=Extra.forbid):
    background_color: Optional[ColorEnum]
    border_color: Optional[ColorEnum]
    border_width: Optional[confloat(ge=0, le=100)]
    border_style: Optional[BorderStyleEnum]

    circle: Optional[Circle]
    line: Optional[Line]
    shape: Optional[Shape]
    textbox: Optional[TextBox]
    textbox_nth_child_1: Optional[TextBox]
    textbox_nth_child_2: Optional[TextBox]
    textbox_nth_child_3: Optional[TextBox]

    def getasy(self, parentselector, index=None):
        cleanArgs = []
        if self.background_color:
            cleanArgs.append(
                f"background_color={self.background_color}")
        if self.border_color:
            cleanArgs.append(
                f"border_color={self.border_color}")
        if self.border_width is not None:
            cleanArgs.append(
                f"border_width={self.border_width}")
        if self.border_style:
            cleanArgs.append(
                f"border_style={self.border_style}")
        if cleanArgs:
            return _asystylerule(cleanArgs, index, parentselector,
                                 "elementtype.shape")
        return ""


class TextBox(BaseModel, extra=Extra.forbid):
    color: Optional[ColorEnum]
    font_family: Optional[FontEnum]
    font_size: Optional[confloat(ge=0, le=300)]
    font_weight: Optional[FontWeightEnum]

    def getasy(self, parentselector, index=None):
        cleanArgs = []
        if self.color:
            cleanArgs.append(
                f"color={self.color}")
        if self.font_family:
            postfix = ""
            if (self.font_weight and self.font_weight == FontWeightEnum.bold):
                postfix = "_bold"
            cleanArgs.append(
                f"font_family=font.{self.font_family.name}{postfix}")
        if self.font_size is not None:
            cleanArgs.append(
                f"font_size={self.font_size}")
        if cleanArgs:
            return _asystylerule(cleanArgs, index, parentselector,
                                 "elementtype.textbox")
        return ""


class Circle(BaseModel, extra=Extra.forbid):
    background_color: Optional[ColorEnum]
    border_color: Optional[ColorEnum]
    border_width: Optional[confloat(ge=0, le=100)]
    border_style: Optional[BorderStyleEnum]

    circle: Optional[Circle]
    line: Optional[Line]
    shape: Optional[Shape]
    textbox: Optional[TextBox]

    def getasy(self, parentselector, index=None):
        cleanArgs = []
        if self.background_color:
            cleanArgs.append(
                f"background_color={self.background_color}")
        if self.border_color:
            cleanArgs.append(
                f"border_color={self.border_color}")
        if self.border_width is not None:
            cleanArgs.append(
                f"border_width={self.border_width}")
        if self.border_style:
            cleanArgs.append(
                f"border_style={self.border_style}")
        if cleanArgs:
            return _asystylerule(cleanArgs, index, parentselector,
                                 "elementtype.circle")
        return ""


class FigureCircleStyle(BaseModel, extra=Extra.forbid):
    rotation: Optional[conint(ge=0, le=360)]
    middle: Optional[bool]

    def getasy(self):
        cleanArgs = []
        if self.rotation is not None:
            cleanArgs.append(
                f"degreeStart={self.rotation}")
        if self.middle:
            cleanArgs.append(
             "middle="
             f"{str(self.middle).lower()}")
        return f"registercirclestyle({','.join(cleanArgs)})"


class FigureOrgChartStyle(BaseModel, extra=Extra.forbid):
    landscape: Optional[bool]
    tuck: Optional[bool]
    horizspacing: Optional[confloat(ge=0, le=300)]
    vertspacing: Optional[confloat(ge=0, le=300)]

    def getasy(self):
        cleanArgs = []
        if self.landscape:
            cleanArgs.append(f"landscape={str(self.landscape).lower()}")
        if self.tuck:
            cleanArgs.append(f"tuck={str(self.tuck).lower()}")
        if self.horizspacing is not None:
            cleanArgs.append(
                f"horizspacing={self.horizspacing}")
        if self.vertspacing is not None:
            cleanArgs.append(
                f"vertspacing={self.vertspacing}")
        return f"registerorgchartstyle({','.join(cleanArgs)})"


class Style(BaseModel, extra=Extra.forbid):
    figure_concept_circle: Optional[FigureCircleStyle]
    figure_org_orgchart: Optional[FigureOrgChartStyle]
    circle: Optional[Circle]
    line: Optional[Line]
    shape: Optional[Shape]
    textbox: Optional[TextBox]


class Message(BaseModel, extra=Extra.forbid):
    """ Inputs for the concept/circle figure """

    # [Flake8 raises "syntax error in forward annotation" on regex
    # constraints](https://github.com/samuelcolvin/pydantic/issues/2872)
    data: constr(regex=('^[' +                                 # noqa: F722
                        re.escape(string.printable) + ']+$'),  # noqa: F722
                 min_length=1,
                 # Pydantic v2 will allow us to relax this limit depending
                 # on context (cmdline v api)
                 # https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#validation-context
                 max_length=5000)
    style: Optional[Style]

    def walkstyletree(self, node, parentselector):
        cleanArgs = []

        if (node is None):
            return cleanArgs

        if "figure_concept_circle" in node.dict(exclude_unset=True):
            cleanArgs.append(node.figure_concept_circle.getasy())
        if "figure_org_orgchart" in node.dict(exclude_unset=True):
            cleanArgs.append(node.figure_org_orgchart.getasy())
        if node.circle:
            cleanArgs.append(node.circle.getasy(parentselector))
            myselector = "selector(elementtype.circle)"
            if (parentselector != ""):
                myselector = f"{parentselector}, {myselector}"
            cleanArgs.extend(self.walkstyletree(node.circle, myselector))
        if node.line:
            cleanArgs.append(node.line.getasy(parentselector))
        if node.shape:
            cleanArgs.append(node.shape.getasy(parentselector))
            myselector = "selector(elementtype.shape)"
            if (parentselector != ""):
                myselector = f"{parentselector}, {myselector}"
            cleanArgs.extend(
                    self.walkstyletree(node.shape, myselector))
        if node.textbox:
            cleanArgs.append(node.textbox.getasy(parentselector))
        if "textbox_nth_child_1" in node.dict(exclude_unset=True):
            cleanArgs.append(
                    node.textbox_nth_child_1.getasy(parentselector, 1))
        if "textbox_nth_child_2" in node.dict(exclude_unset=True):
            cleanArgs.append(
                    node.textbox_nth_child_2.getasy(parentselector, 2))
        if "textbox_nth_child_3" in node.dict(exclude_unset=True):
            cleanArgs.append(
                    node.textbox_nth_child_3.getasy(parentselector, 3))

        return cleanArgs

    def getasy(self):
        cleanArgs = []
        if self.style:
            cleanArgs = self.walkstyletree(self.style, "")
        return f"{';'.join(cleanArgs)};"


# [Postponed annotations - pydantic]
# (https://pydantic-docs.helpmanual.io/usage/postponed_annotations/)
Shape.update_forward_refs()
Circle.update_forward_refs()
