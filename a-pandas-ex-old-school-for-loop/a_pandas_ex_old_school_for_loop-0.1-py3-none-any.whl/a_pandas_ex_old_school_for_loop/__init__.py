from functools import partial
from pandas.core.frame import DataFrame, Series
from flatten_any_dict_iterable_or_whatsoever import (
    get_from_original_iter,
    set_in_original_iter,
)
from nestednop import NestedNop
from useful_functions_easier_life import NamedFunction


def get_item_val(df, slicy, item):
    los = df.iloc.__getitem__((slicy, item[0][-1][0]))
    if len(item[0][-1]) > 2:
        return get_from_original_iter(
            (df.iloc.__getitem__((slicy, item[0][-1][0]))).item(), item[0][-1][2:]
        )
    return getattr(los, "item")()


def set_item_val(df, slicy, item, value):
    if len(item[0][-1]) == 2:
        los = df.iloc.__setitem__((slicy, item[0][-1][0]), value)
    else:
        set_in_original_iter(
            (df.iloc.__getitem__((slicy, item[0][-1][0]))).item(),
            item[0][-1][2:],
            value,
        )


def get_setable_iter_df(df):
    """
    from a_pandas_ex_old_school_for_loop import pd_add_old_school_for_loop
    pd_add_old_school_for_loop()
    import pandas as pd
    df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

    df
    Out[3]:
         PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    0              1         0       3  ...   7.2500   NaN         S
    1              2         1       1  ...  71.2833   C85         C
    2              3         1       3  ...   7.9250   NaN         S
    3              4         1       1  ...  53.1000  C123         S
    4              5         0       3  ...   8.0500   NaN         S
    ..           ...       ...     ...  ...      ...   ...       ...
    886          887         0       2  ...  13.0000   NaN         S
    887          888         1       1  ...  30.0000   B42         S
    888          889         0       3  ...  23.4500   NaN         S
    889          890         1       1  ...  30.0000  C148         C
    890          891         0       3  ...   7.7500   NaN         Q
    [891 rows x 12 columns]


    for item in df.ds_set_values_with_loop():
        try:
            if item['get_value']() > 2:
                item['set_value'](10000000)
        except Exception:
            continue


    df
    Out[5]:
         PassengerId  Survived    Pclass  ...        Fare Cabin  Embarked
    0              1         0  10000000  ...  10000000.0   NaN         S
    1              2         1         1  ...  10000000.0   C85         C
    2       10000000         1  10000000  ...  10000000.0   NaN         S
    3       10000000         1         1  ...  10000000.0  C123         S
    4       10000000         0  10000000  ...  10000000.0   NaN         S
    ..           ...       ...       ...  ...         ...   ...       ...
    886     10000000         0         2  ...  10000000.0   NaN         S
    887     10000000         1         1  ...  10000000.0   B42         S
    888     10000000         0  10000000  ...  10000000.0   NaN         S
    889     10000000         1         1  ...  10000000.0  C148         C
    890     10000000         0  10000000  ...  10000000.0   NaN         Q
    [891 rows x 12 columns]

    """
    yield from [x[1] for x in get_dict_for_writing(df).items()]


def get_setable_iter_series(df):
    """
    from a_pandas_ex_old_school_for_loop import pd_add_old_school_for_loop
    pd_add_old_school_for_loop()
    import pandas as pd
    df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

    df
    Out[3]:
         PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    0              1         0       3  ...   7.2500   NaN         S
    1              2         1       1  ...  71.2833   C85         C
    2              3         1       3  ...   7.9250   NaN         S
    3              4         1       1  ...  53.1000  C123         S
    4              5         0       3  ...   8.0500   NaN         S
    ..           ...       ...     ...  ...      ...   ...       ...
    886          887         0       2  ...  13.0000   NaN         S
    887          888         1       1  ...  30.0000   B42         S
    888          889         0       3  ...  23.4500   NaN         S
    889          890         1       1  ...  30.0000  C148         C
    890          891         0       3  ...   7.7500   NaN         Q
    [891 rows x 12 columns]


    for item in df.PassengerId.ds_set_values_with_loop():
        try:
            if item['get_value']() > 2:
                item['set_value'](10000000)
        except Exception:
            continue

    df
    Out[3]:
         PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    0              1         0       3  ...   7.2500   NaN         S
    1              2         1       1  ...  71.2833   C85         C
    2       10000000         1       3  ...   7.9250   NaN         S
    3       10000000         1       1  ...  53.1000  C123         S
    4       10000000         0       3  ...   8.0500   NaN         S
    ..           ...       ...     ...  ...      ...   ...       ...
    886     10000000         0       2  ...  13.0000   NaN         S
    887     10000000         1       1  ...  30.0000   B42         S
    888     10000000         0       3  ...  23.4500   NaN         S
    889     10000000         1       1  ...  30.0000  C148         C
    890     10000000         0       3  ...   7.7500   NaN         Q
    [891 rows x 12 columns]
    """
    yield from [x[1] for x in get_dict_for_writing(df.to_frame()).items()]


def get_dict_for_writing(df):
    dicttoedit = {
        ini: {
            "path_iloc": item[0][-1],
            "path_loc": item[1][-1],
            "get_value": NamedFunction(
                name="get_value",
                execute_function=partial(
                    get_item_val, df, slice(item[0][-1][1], item[0][-1][1] + 1), item
                ),
                name_function=lambda: " ",
                str_prefix=f"Original Value: {item[-1][2:][0]} ",
                str_suffix="",
            ),
            "set_value": NamedFunction(
                name="set_value",
                execute_function=partial(
                    set_item_val, df, slice(item[0][-1][1], item[0][-1][1] + 1), item
                ),
                name_function=lambda: " ",
                str_prefix=f"Path: {item[-1][-1]} ",
                str_suffix="",
            ),
        }
        for ini, item in enumerate(
            NestedNop(
                iterable=df, disable_str_repr=True, pandas_loc_or_iloc="iloc"
            ).iterable_list
        )
    }

    return dicttoedit


def pd_add_old_school_for_loop():
    DataFrame.ds_set_values_with_loop = get_setable_iter_df
    Series.ds_set_values_with_loop = get_setable_iter_series
