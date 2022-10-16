from typing import Callable, Tuple, Dict, Union
import re
from math import log10
import sigfig

Number = Union[int, float]
FormatFunction = Callable[[Number], str]
ExpExprStyle = {"latex": "latex", "word": "word", "original": "original"}
ExpExprTranslator = Callable[[str], str]

exp_regex: re.Pattern = re.compile(r".*[eE]([+-]?)(\d+)")


def parse_exp_expr(x: str) -> Tuple[str, int]:
    match = exp_regex.match(x)
    if match:
        sign: str = match.group(1)
        exponent: str = match.group(2)
        exp_expr_len: int = len(exponent)+len(sign)+1
        return x[:-exp_expr_len], int(exponent)*(-1 if sign == "-" else 1)
    else:
        return x, 0


def latexify_exp_expr(x: str) -> str:
    mantissa, exponent = parse_exp_expr(x)
    if exponent == 0:
        return mantissa
    else:
        return "$"+mantissa + r"\times10^{" + str(exponent) + "}$"


def wordify_exp_expr(x: str) -> str:
    mantissa, exponent = parse_exp_expr(x)
    if exponent == 0:
        return mantissa
    else:
        return mantissa + r"\times10^" + str(exponent)


def do_nothing_with_exp_expr(x: str) -> str:
    return x


exp_expr_translators: Dict[str, ExpExprTranslator] = {
    "latex": latexify_exp_expr,
    "word": wordify_exp_expr,
    "original": do_nothing_with_exp_expr,
}


def create_f_format(digits: str) -> FormatFunction:
    return lambda x: ("{:."+str(digits)+"f}").format(x)


def create_g_format(digits: str) -> FormatFunction:
    return lambda x: ("{:."+str(digits)+"g}").format(x)


def create_e_format(digits: str) -> FormatFunction:
    return lambda x: ("{:."+str(digits)+"e}").format(x)


def create_force_f_format(digits: str) -> FormatFunction:
    return lambda x: sigfig.round(str(x), decimals=int(digits), warn=False)


def create_translated_e_format(digits: str, style: str = "original") -> FormatFunction:
    e_format: FormatFunction = create_e_format(digits)
    exp_expr_translator: ExpExprTranslator = exp_expr_translators[style]

    def format(x):
        e_formatted: str = e_format(x)
        translated: str = exp_expr_translator(e_formatted)
        return translated

    return format


def create_translated_g_format(digits: str, style: str = "original") -> FormatFunction:
    g_format: FormatFunction = create_g_format(digits)
    exp_expr_translator: ExpExprTranslator = exp_expr_translators[style]

    def format(x):
        di: int = int(log10(abs(x)))
        if di >= int(digits):
            g_formatted: str = g_format(x)
            translated: str = exp_expr_translator(g_formatted)
            return translated
        return sigfig.round(str(x), sigfigs=digits, warn=False)

    return format
