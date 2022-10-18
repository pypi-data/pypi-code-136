import re
import types

import pandas as pd
from pandas.core.frame import DataFrame
from pandas.errors import SettingWithCopyWarning
from friendly_traceback.about_warnings import WarningInfo, get_warning_parser
from friendly_traceback.info_variables import get_object_from_name
from friendly_traceback.typing_info import CauseInfo

parser = get_warning_parser(SettingWithCopyWarning)


@parser.add
def setting_with_copy_warning(message: str, warning_data: WarningInfo) -> CauseInfo:
    statement = re.sub(r"\s+", "", warning_data.problem_statement)
    # Unfortunately, IPython/Jupyter use some temporary files which are not
    # available after the fact to obtain the statement.
    if not statement:
        source = "".join(warning_data.lines)
        statement = re.sub(r"\s+", "", source)

    pattern_direct = re.compile(r"(.*)\.loc\[(.*)\]\[(.*)\].*")
    pattern_indirect_1 = re.compile(r"(.*)\.loc\[(.*)\].*")
    pattern_indirect_2 = re.compile(r"(.*)\[(.*)\].*")
    match = re.match(pattern_direct, statement)
    match_1 = re.match(pattern_indirect_1, statement)
    match_2 = re.match(pattern_indirect_2, statement)
    if match:
        return direct_indexing(
            statement, match[1].strip(), match[2].strip(), match[3].strip()
        )
    if match_1:
        series = match_1[1].strip()
        series_obj = get_object_from_name(series, warning_data.frame)
        if isinstance(series_obj, pd.Series):
            return indirect_indexing(
                series, match_1[2].strip(), warning_data.frame, loc_2=".loc"
            )
    elif match_2:
        series = match_2[1].strip()
        series_obj = get_object_from_name(series, warning_data.frame)
        if isinstance(series_obj, pd.Series):
            return indirect_indexing(
                series, match_2[2].strip(), warning_data.frame, loc_1=".loc"
            )
    return {}


def direct_indexing(
    statement: str, dataframe_name: str, index_1: str, index_2: str
) -> CauseInfo:
    cause = (
        "You used direct chained indexing of a dataframe which made a copy\n"
        "of the original content of the dataframe. If you try to assign a value\n"
        "to that copy, the original dataframe will not be modified.\n"
        "Instead of doing a direct chained indexing\n\n"
        "    {dataframe_name}.loc[{index_1}][{index_2}] ...\n\n"
        " try:\n\n"
        "    {dataframe_name}.loc[{index_1}, {index_2}] ...\n"
    ).format(
        statement=statement,
        dataframe_name=dataframe_name,
        index_1=index_1,
        index_2=index_2,
    )
    return {"cause": cause}


def indirect_indexing(
    series_name: str,
    index: str,
    frame: types.FrameType,
    loc_1: str = "",
    loc_2: str = "",
) -> CauseInfo:
    names = find_all_dataframes(frame)
    if not names:
        return {}
    basic_cause = (
        "I suspect that you used indirect chained indexing of a dataframe.\n"
        "First, you likely created a series using something like:\n\n"
        "    {series_name} = {dataframe_name}{loc_1}[...]\n\n"
        "This made a copy of the data contained in the dataframe.\n"
        "Next, you indexed that copy\n\n"
        "    {series_name}{loc_2}[{index}]\n\n"
        "This had no effect on the original dataframe.\n"
        "If your goal is to modify the value of the original dataframe,\n"
        "try something like the following instead:\n\n"
        "    {dataframe_name}.loc[..., {index}]\n"
    )
    name = names.pop()
    if len(names) == 0:
        cause = basic_cause.format(
            series_name=series_name,
            dataframe_name=name,
            index=index,
            loc_1=loc_1,
            loc_2=loc_2,
        )
    else:
        names.add(name)
        intro = (
            "In your code, you have the following dataframes: `{df}`.\n"
            "I do not know which one is causing the problem here;\n"
            "I will use the name `{name}` as an example.\n\n"
        ).format(df=names, name=name)
        cause = intro + basic_cause.format(
            series_name=series_name,
            dataframe_name=name,
            index=index,
            loc_1=loc_1,
            loc_2=loc_2,
        )
    return {"cause": cause}


def find_all_dataframes(frame: types.FrameType) -> set:
    dataframes = {
        name for name in frame.f_locals if isinstance(frame.f_locals[name], DataFrame)
    }
    gl_dataframes = {
        name for name in frame.f_globals if isinstance(frame.f_globals[name], DataFrame)
    }
    return dataframes.union(gl_dataframes)
