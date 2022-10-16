from typing import Callable, List, Optional, Dict, Collection, Any, Union
from pandas import DataFrame
from pandas.io import clipboard
from pandas.io.formats.style import Styler
import re
import tempfile
import os
from pathlib import Path
from yagamee import formats
from yagamee.formats import FormatFunction, ExpExprStyle

DictData = Dict[str, Collection[Any]]
ListishData = Collection[Any]


def to_dataframe(data: Union[DataFrame, DictData, ListishData, Styler]) -> DataFrame:
    if(isinstance(data, DataFrame)):
        pass
    elif(isinstance(data, Styler)):
        data = data.data
    else:
        data = DataFrame(data)
    return data


DataFrameOrStyler = Union[DataFrame, Styler]


def to_styler(table: DataFrameOrStyler) -> Styler:
    if(isinstance(table, DataFrame)):
        table = table.style
    else:
        pass
    return table


sigfig_notation_regex: re.Pattern = re.compile(r"f\d+|g\d+|e\d+|G\d+|E\d+|F\d+|\s")
Formatter = Dict[str, FormatFunction]


def create_formatter(notation: Optional[str], columns: List[str], exp_expr_style: ExpExprStyle = "original") -> Optional[Formatter]:
    if notation is None:
        return None
    formatter: Dict = {}
    notation = notation or ""
    format_order_s = sigfig_notation_regex.findall(notation)
    for format_order, column_name in zip(format_order_s, list(columns)):
        format_method: str = format_order[0]
        format_param: str = format_order[1:]
        format: FormatFunction = None
        if(format_method == "f"):
            format = formats.create_f_format(format_param)
        elif(format_method == "g"):
            format = formats.create_g_format(format_param)
        elif(format_method == "e"):
            format = formats.create_e_format(format_param)
        elif(format_method == "G"):
            format = formats.create_translated_g_format(
                format_param, exp_expr_style)
        elif(format_method == "E"):
            format = formats.create_translated_e_format(
                format_param, exp_expr_style)
        elif(format_method == "F"):
            format = formats.create_force_f_format(format_param)
        if format:
            formatter[column_name] = format
    return formatter


def format_sigfig(table: DataFrameOrStyler, notation: Optional[str], exp_expr_style: ExpExprStyle = "original") -> Styler:
    formatter: Optional[Formatter] = create_formatter(
        notation, table.columns, exp_expr_style)
    if formatter:
        table: DataFrame = to_dataframe(table).copy()
        for column_name, format in formatter.items():
            table[column_name] = table[column_name].transform(format)
    styler = to_styler(table)
    return styler


def copy_as_latex(
    table: DataFrame,
    sigfig_notation: Optional[str] = None,
    show_index: bool = False,
) -> Styler:
    styler: Styler = format_sigfig(table, sigfig_notation, "latex")
    if not show_index:
        styler = styler.hide()
    latex: str = styler.to_latex(hrules=True,position_float="centering",caption="-----")
    clipboard.copy(latex)
    return styler


excel_file_path: str = str(
    Path(tempfile.gettempdir()) / "yagamee_temp_table.xlsx")


def preview_in_excel(
    table: DataFrameOrStyler,
    sigfig_notation: Optional[str] = None
) -> None:
    styler: Styler = format_sigfig(table, sigfig_notation, "word")
    styler.to_excel(excel_file_path)
    os.startfile(excel_file_path)
