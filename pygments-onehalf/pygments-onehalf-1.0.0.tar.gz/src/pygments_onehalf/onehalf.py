from typing import Any, Dict, Type, Union

from pygments.style import Style
from pygments.token import Comment, Keyword, Name, Number, Operator, String, Text


class DarkColors:
    black = "#282c34"
    red = "#e06c75"
    green = "#98c379"
    yellow = "#e5c07b"
    blue = "#61afef"
    magenta = "#c678dd"
    cyan = "#56b6c2"
    white = "#dcdfe4"
    foreground = "#dcdfe4"
    background = "#282c34"
    comment = "#5c6370"


class LightColors:
    black = "#383a42"
    red = "#e45649"
    green = "#50a14f"
    yellow = "#c18401"
    blue = "#0184bc"
    magenta = "#a626a4"
    cyan = "#0997b3"
    white = "#fafafa"
    foreground = "#383a42"
    background = "#fafafa"
    comment = "#a0a1a7"


def make_styles(colors: Union[Type[DarkColors], Type[LightColors]]) -> Dict[Any, str]:
    return {
        Comment: colors.comment,
        Keyword.Constant: colors.yellow,
        Keyword: colors.magenta,
        Name.Builtin: colors.blue,
        Name.Class: colors.yellow,
        Name.Decorator: colors.blue,
        Name.Function: colors.blue,
        Name: colors.foreground,
        Number: colors.yellow,
        Operator: colors.magenta,
        String.Affix: colors.magenta,
        String.Interpol: colors.yellow,
        String: colors.green,
        Text: colors.foreground,
    }


class OneHalfDark(Style):
    default_style = ""
    background_color = DarkColors.background
    styles = make_styles(DarkColors)


class OneHalfLight(Style):
    default_style = ""
    background_color = LightColors.background
    styles = make_styles(LightColors)
