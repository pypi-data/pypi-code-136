from typing import Union
import numpy as np
from flatten_everything import flatten_everything
from pandas.core.frame import DataFrame, Series
from cprinter import TC
from a_pandas_ex_less_memory_more_speed import string_to_mixed_dtypes
import pandas as pd
from aa_pandas_ex_plode_tool import qq_s_isnan


def series_to_dataframe(
    df: Union[pd.Series, pd.DataFrame]
) -> (Union[pd.Series, pd.DataFrame], bool):
    dataf = df.copy()
    isseries = False
    if isinstance(dataf, pd.Series):
        columnname = dataf.name
        dataf = dataf.to_frame()

        try:
            dataf.columns = [columnname]
        except Exception:
            dataf.index = [columnname]
            dataf = dataf.T
        isseries = True

    return dataf, isseries


def isiter(objectX) -> bool:
    if isinstance(objectX, (np.ndarray, pd.DataFrame, pd.Series)):
        return True
    if isinstance(objectX, (str, bytes)):
        return False
    try:
        some_object_iterator = iter(objectX)
        return True
    except TypeError as te:
        return False


def _delete_duplicates_nested(variable):
    tempdict = {}
    try:
        if isiter(variable):
            for _ in variable:
                try:
                    tempdict[_] = _
                except Exception:
                    tempdict[str(_)] = _
            nomoredupli = [x[1] for x in tempdict.items()]
            return nomoredupli
        else:
            return variable

    except Exception:
        return variable


def sort_dtypes(dframe, col, lambda_function):
    df = dframe.copy()
    df[col] = string_to_mixed_dtypes(df[col])
    df["___dtypesgroup___"] = df[col].map(lambda x: str(type(x)))
    goodvalues = []
    for name, values in df.groupby("___dtypesgroup___"):
        try:
            values_tmp = values.copy()
            values_tmp["____True_____False_____"] = values_tmp[col].map(lambda_function)
            sortedvaluesdf = values_tmp.loc[
                values_tmp["____True_____False_____"] == True
            ]
            sortedvalues = sortedvaluesdf.index.to_list().copy()
            goodvalues.extend(sortedvalues)
        except Exception:
            pass
    indexer = _delete_duplicates_nested(goodvalues)
    return indexer


def get_loc(
    df,
    col,
    value,
    action,
    ignore_exceptions=True,
    ignore_na=True,
    negative=False,
    print_exceptions=False,
):

    dfx = df.copy()
    got_right_indexer_already = False
    if action == "isna":
        ignore_na = False
    if ignore_na is True:
        dfx = dfx.dropna(subset=col)
    try:
        if action == "<":
            try:
                indexer = np.where(dfx.loc(axis=1)._get_label(col, 1).lt(value))
                if not np.any(indexer):
                    indexer = sort_dtypes(df, col, lambda_function=lambda x: x < value)
                    got_right_indexer_already = True
            except Exception as F:
                if print_exceptions:
                    print(F)
                indexer = sort_dtypes(df, col, lambda_function=lambda x: x < value)
                got_right_indexer_already = True
        elif action == "<=":
            try:
                indexer = np.where(dfx.loc(axis=1)._get_label(col, 1).le(value))
                if not np.any(indexer):
                    indexer = sort_dtypes(df, col, lambda_function=lambda x: x <= value)
                    got_right_indexer_already = True
            except Exception as F:
                if print_exceptions:
                    print(F)
                indexer = sort_dtypes(df, col, lambda_function=lambda x: x <= value)
                got_right_indexer_already = True
        elif action == "==":
            try:
                indexer = np.where(dfx.loc(axis=1)._get_label(col, 1).eq(value))
                if not np.any(indexer):
                    indexer = sort_dtypes(df, col, lambda_function=lambda x: x == value)
                    got_right_indexer_already = True
            except Exception as F:
                if print_exceptions:
                    print(F)

                indexer = sort_dtypes(df, col, lambda_function=lambda x: x == value)
                got_right_indexer_already = True
        elif action == "!=":
            try:
                indexer = np.where(dfx.loc(axis=1)._get_label(col, 1).ne(value))
                if not np.any(indexer):
                    indexer = sort_dtypes(df, col, lambda_function=lambda x: x != value)
                    got_right_indexer_already = True
            except Exception as F:
                if print_exceptions:
                    print(F)
                indexer = sort_dtypes(df, col, lambda_function=lambda x: x != value)
                got_right_indexer_already = True
        elif action == ">=":
            try:
                indexer = np.where(dfx.loc(axis=1)._get_label(col, 1).ge(value))
                if not np.any(indexer):
                    indexer = sort_dtypes(df, col, lambda_function=lambda x: x >= value)
                    got_right_indexer_already = True
            except Exception as F:
                if print_exceptions:
                    print(F)
                indexer = sort_dtypes(df, col, lambda_function=lambda x: x >= value)
                got_right_indexer_already = True
        elif action == ">":
            try:
                indexer = np.where(dfx.loc(axis=1)._get_label(col, 1).gt(value))
                if not np.any(indexer):
                    indexer = sort_dtypes(df, col, lambda_function=lambda x: x > value)
                    got_right_indexer_already = True
            except Exception as F:
                if print_exceptions:
                    print(F)
                indexer = sort_dtypes(df, col, lambda_function=lambda x: x > value)
                got_right_indexer_already = True
        elif action == "in":
            try:
                indexer = np.where(dfx.loc(axis=1)._get_label(col, 1).isin(value))
            except Exception as F:
                if print_exceptions:
                    print(F)
                indexer = sort_dtypes(df, col, lambda_function=lambda x: x in value)
                got_right_indexer_already = True
        elif action == "re":
            indexer = np.where(
                dfx.loc(axis=1)
                ._get_label(col, 1)
                .astype("string")
                .str.contains(value, regex=True)
            )

        elif action == "str":
            indexer = np.where(
                dfx.loc(axis=1)
                ._get_label(col, 1)
                .astype("string")
                .str.contains(value, regex=False)
            )

        elif action == "isna":
            indexer = np.where(
                dfx.loc(axis=1)
                ._get_label(col, 1)
                .map(
                    lambda q: qq_s_isnan(
                        q,
                        include_na_strings=True,
                        nan_back=False,
                        include_empty_iters=True,
                    )
                )
            )

        elif action == "in_iter":
            if isinstance(value, tuple):
                value = list(value)
            elif not isinstance(value, list):
                value = [value]
            indexer = np.where(
                dfx.loc(axis=1)
                ._get_label(col, 1)
                .map(lambda _: list(set(value) & set(flatten_everything(_))))
            )
        else:
            indexer = range(len(df))
        if isinstance(indexer, tuple):
            indexer = indexer[0]
        if got_right_indexer_already is False:
            indexer = dfx.index[indexer]
        if negative:
            indexer = list(set(dfx.index) - set(indexer))

        return df.loc[indexer], indexer
    except Exception as Fehler:
        if print_exceptions:
            print(TC(f"{col}, {action}, {value}").fg_black.bg_red)

            print(TC(f"{Fehler}").bg_black.fg_red)
        if ignore_exceptions:
            return df, None
        else:
            raise NaException(f"EXCEPTION: {Fehler} ") from Fehler


def positive_conditions_and(
    df,
    *args,
    ignore_exceptions=True,
    ignore_na=True,
    print_exceptions=True,
    replace=None,
):
    return condition_and(
        df,
        condition=args,
        negative=False,
        ignore_exceptions=ignore_exceptions,
        ignore_na=ignore_na,
        print_exceptions=print_exceptions,
        replace=replace,
    )


def positive_conditions_or(
    df,
    *args,
    ignore_exceptions=True,
    ignore_na=True,
    print_exceptions=True,
    replace=None,
):
    return condition_or(
        df,
        condition=args,
        negative=False,
        ignore_exceptions=ignore_exceptions,
        ignore_na=ignore_na,
        print_exceptions=print_exceptions,
        replace=replace,
    )


def negative_conditions_and(
    df,
    *args,
    ignore_exceptions=True,
    ignore_na=True,
    print_exceptions=True,
    replace=None,
):
    return condition_and(
        df,
        condition=args,
        negative=True,
        ignore_exceptions=ignore_exceptions,
        ignore_na=ignore_na,
        print_exceptions=print_exceptions,
        replace=replace,
    )


def negative_conditions_or(
    df,
    *args,
    ignore_exceptions=True,
    ignore_na=True,
    print_exceptions=True,
    replace=None,
):
    return condition_or(
        df,
        condition=args,
        negative=True,
        ignore_exceptions=ignore_exceptions,
        ignore_na=ignore_na,
        print_exceptions=print_exceptions,
        replace=replace,
    )


def condition2three(condition, isseries, dfcolumns=None):
    if isseries:
        condition_temp = []
        for cmd in condition:
            newc = dfcolumns + list(cmd)
            condition_temp.append(tuple(newc))
        condition = condition_temp.copy()
    return [
        x if len(x).__eq__(3) else tuple(list(x).__add__([None])) for x in condition
    ]


def condition_and(
    df,
    condition,
    negative=False,
    ignore_exceptions=True,
    ignore_na=True,
    print_exceptions=True,
    replace=None,
):

    gleich, isseries = series_to_dataframe(df)
    dfs = gleich.copy()
    condition = condition2three(condition, isseries, gleich.columns.to_list())

    for colo, ope, val in condition:
        if replace is None:
            gleich, indexer = get_loc(
                gleich,
                col=colo,
                value=val,
                action=ope,
                negative=negative,
                ignore_exceptions=ignore_exceptions,
                ignore_na=ignore_na,
                print_exceptions=print_exceptions,
            )
        else:
            gleich, indexer = get_loc(
                gleich,
                col=colo,
                value=val,
                action=ope,
                negative=negative,
                ignore_exceptions=ignore_exceptions,
                ignore_na=ignore_na,
                print_exceptions=print_exceptions,
            )
            dfs.loc[indexer, colo] = replace

    if replace is not None:

        if isseries:
            try:
                return dfs[dfs.columns[0]]
            except Exception:
                return dfs
        return dfs
    if isseries:
        return gleich[gleich.columns[0]]
    return gleich


def condition_or(
    df,
    condition,
    negative=False,
    ignore_exceptions=True,
    ignore_na=True,
    print_exceptions=True,
    replace=None,
):

    gleich2, isseries = series_to_dataframe(df)
    df_ = gleich2.copy()
    condition = condition2three(condition, isseries, gleich2.columns.to_list())

    allgleichs = []
    for colo, ope, val in condition:
        if replace is None:
            ergi1, ergi2 = get_loc(
                gleich2,
                col=colo,
                value=val,
                action=ope,
                negative=negative,
                ignore_exceptions=ignore_exceptions,
                ignore_na=ignore_na,
                print_exceptions=print_exceptions,
            )
        else:
            ergi1, ergi2 = get_loc(
                gleich2,
                col=colo,
                value=val,
                action=ope,
                negative=negative,
                ignore_exceptions=ignore_exceptions,
                ignore_na=ignore_na,
                print_exceptions=print_exceptions,
            )
            df_.loc[ergi2, colo] = replace
        allgleichs.extend(ergi2.copy())
    if replace is None:
        finaldf = df_.loc[list(set(list((flatten_everything(allgleichs)))))]
        if isseries:
            try:
                return finaldf[finaldf.columns[0]]
            except Exception:
                pass
        return finaldf
    else:
        if isseries:
            try:
                return df_[df_.columns[0]]
            except Exception:
                pass
        return df_


class NaException(Exception):
    pass


def pd_add_easy_loc():
    DataFrame.loc_positive_and = positive_conditions_and
    DataFrame.loc_positive_or = positive_conditions_or
    DataFrame.loc_negative_and = negative_conditions_and
    DataFrame.loc_negative_or = negative_conditions_or
    Series.loc_positive_and = positive_conditions_and
    Series.loc_positive_or = positive_conditions_or
    Series.loc_negative_and = negative_conditions_and
    Series.loc_negative_or = negative_conditions_or
    Series.shortloc_greater = lambda dframe, x: positive_conditions_and(
        dframe, (">", x)
    )
    Series.shortloc_greater_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, (">", x), replace=replace_
    )
    Series.shortloc_greater_or_equal = lambda dframe, x: positive_conditions_and(
        dframe, (">=", x)
    )
    Series.shortloc_less = lambda dframe, x: positive_conditions_and(dframe, ("<", x))
    Series.shortloc_less_or_equal = lambda dframe, x: positive_conditions_and(
        dframe, ("<=", x)
    )
    Series.shortloc_equal = lambda dframe, x: positive_conditions_and(dframe, ("==", x))
    Series.shortloc_not_equal = lambda dframe, x: positive_conditions_and(
        dframe, ("!=", x)
    )
    Series.shortloc_isin = lambda dframe, x: positive_conditions_and(dframe, ("in", x))
    Series.shortloc_regex = lambda dframe, x: positive_conditions_and(dframe, ("re", x))
    Series.shortloc_in_iter = lambda dframe, x: positive_conditions_and(
        dframe, ("in_iter", x)
    )
    Series.shortloc_str = lambda dframe, x: positive_conditions_and(dframe, ("str", x))
    Series.shortloc_isna = lambda dframe: positive_conditions_and(
        dframe, ("isna", None)
    )

    Series.shortloc_not_isin = lambda dframe, x: negative_conditions_and(
        dframe, ("in", x)
    )
    Series.shortloc_not_regex = lambda dframe, x: negative_conditions_and(
        dframe, ("re", x)
    )
    Series.shortloc_not_in_iter = lambda dframe, x: negative_conditions_and(
        dframe, ("in_iter", x)
    )
    Series.shortloc_not_str = lambda dframe, x: negative_conditions_and(
        dframe, ("str", x)
    )
    Series.shortloc_not_isna = lambda dframe: negative_conditions_and(
        dframe, ("isna", None)
    )

    DataFrame.shortloc_greater = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, ">", x)
    )
    DataFrame.shortloc_greater_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, ">", x), replace=replace_
    )
    DataFrame.shortloc_greater_or_equal = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, ">=", x)
    )
    DataFrame.shortloc_greater_or_equal_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, ">=", x), replace=replace_
    )
    DataFrame.shortloc_less = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, "<", x)
    )
    DataFrame.shortloc_less_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, "<", x), replace=replace_
    )
    DataFrame.shortloc_less_or_equal = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, "<=", x)
    )
    DataFrame.shortloc_less_or_equal_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, "<=", x), replace=replace_
    )
    DataFrame.shortloc_equal = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, "==", x)
    )
    DataFrame.shortloc_not_equal = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, "!=", x)
    )
    DataFrame.shortloc_isin = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, "in", x)
    )
    DataFrame.shortloc_regex = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, "re", x)
    )
    DataFrame.shortloc_in_iter = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, "in_iter", x)
    )
    DataFrame.shortloc_str = lambda dframe, col, x: positive_conditions_and(
        dframe, (col, "str", x)
    )
    DataFrame.shortloc_isna = lambda dframe, col: positive_conditions_and(
        dframe, (col, "isna", None)
    )

    DataFrame.shortloc_not_isin = lambda dframe, col, x: negative_conditions_and(
        dframe, (col, "in", x)
    )
    DataFrame.shortloc_not_regex = lambda dframe, col, x: negative_conditions_and(
        dframe, (col, "re", x)
    )
    DataFrame.shortloc_not_in_iter = lambda dframe, col, x: negative_conditions_and(
        dframe, (col, "in_iter", x)
    )
    DataFrame.shortloc_not_str = lambda dframe, col, x: negative_conditions_and(
        dframe, (col, "str", x)
    )
    DataFrame.shortloc_not_isna = lambda dframe, col: negative_conditions_and(
        dframe, (col, "isna", None)
    )
    DataFrame.shortloc_equal_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, "==", x), replace=replace_
    )
    DataFrame.shortloc_not_equal_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, "!=", x), replace=replace_
    )
    DataFrame.shortloc_isin_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, "in", x), replace=replace_
    )
    DataFrame.shortloc_regex_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, "re", x), replace=replace_
    )
    DataFrame.shortloc_in_iter_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, "in_iter", x), replace=replace_
    )
    DataFrame.shortloc_str_replace = lambda dframe, col, x, replace_: positive_conditions_and(
        dframe, (col, "str", x), replace=replace_
    )
    DataFrame.shortloc_isna_replace = lambda dframe, col, replace_: positive_conditions_and(
        dframe, (col, "isna", None), replace=replace_
    )
    DataFrame.shortloc_not_isin_replace = lambda dframe, col, x, replace_: negative_conditions_and(
        dframe, (col, "in", x), replace=replace_
    )
    DataFrame.shortloc_not_regex_replace = lambda dframe, col, x, replace_: negative_conditions_and(
        dframe, (col, "re", x), replace=replace_
    )
    DataFrame.shortloc_not_in_iter_replace = lambda dframe, col, x, replace_: negative_conditions_and(
        dframe, (col, "in_iter", x), replace=replace_
    )
    DataFrame.shortloc_not_str_replace = lambda dframe, col, x, replace_: negative_conditions_and(
        dframe, (col, "str", x), replace=replace_
    )
    DataFrame.shortloc_not_isna_replace = lambda dframe, col, replace_: negative_conditions_and(
        dframe, (col, "isna", None), replace=replace_
    )

    Series.shortloc_greater_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, (">", x), replace=replace_
    )
    Series.shortloc_greater_or_equal_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, (">=", x), replace=replace_
    )
    Series.shortloc_less_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, ("<", x), replace=replace_
    )
    Series.shortloc_less_or_equal_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, ("<=", x), replace=replace_
    )
    Series.shortloc_equal_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, ("==", x), replace=replace_
    )
    Series.shortloc_not_equal_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, ("!=", x), replace=replace_
    )
    Series.shortloc_isin_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, ("in", x), replace=replace_
    )
    Series.shortloc_regex_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, ("re", x), replace=replace_
    )
    Series.shortloc_in_iter_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, ("in_iter", x), replace=replace_
    )
    Series.shortloc_str_replace = lambda dframe, x, replace_: positive_conditions_and(
        dframe, ("str", x), replace=replace_
    )
    Series.shortloc_isna_replace = lambda dframe, replace_: positive_conditions_and(
        dframe, ("isna", None), replace=replace_
    )
    Series.shortloc_not_isin_replace = lambda dframe, x, replace_: negative_conditions_and(
        dframe, ("in", x), replace=replace_
    )
    Series.shortloc_not_regex_replace = lambda dframe, x, replace_: negative_conditions_and(
        dframe, ("re", x), replace=replace_
    )
    Series.shortloc_not_in_iter_replace = lambda dframe, x, replace_: negative_conditions_and(
        dframe, ("in_iter", x), replace=replace_
    )
    Series.shortloc_not_str_replace = lambda dframe, x, replace_: negative_conditions_and(
        dframe, ("str", x), replace=replace_
    )
    Series.shortloc_not_isna_replace = lambda dframe, replace_: negative_conditions_and(
        dframe, ("isna", None), replace=replace_
    )
