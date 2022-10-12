from typing import Union
import pandas as pd
from pandas.core.frame import DataFrame, Series

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


def update_from_other_dataframe(
    df: Union[pd.Series, pd.DataFrame], forupdate: Union[pd.Series, pd.DataFrame],
        update_existing_values=True, add_new_columns=True,add_new_rows=True
) -> Union[pd.Series, pd.DataFrame]:
    """
    Update a DataFrame/Series with the values of another.


    df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                       columns=['a', 'b', 'c'])
    df2 = pd.DataFrame(np.array([[11, 2, 3], [4, 55, 6], [7, 8, 9], [17, 2, 93]]),
                       columns=['a', 'x', 'y'])


    df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=False,add_new_rows=False)

    df1
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    df2
        a   x   y
    0  11   2   3
    1   4  55   6
    2   7   8   9
    3  17   2  93
    df3
        a  b  c
    0  11  2  3
    1   4  5  6
    2   7  8  9




    df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=True,add_new_rows=False)

    df1
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    df2
        a   x   y
    0  11   2   3
    1   4  55   6
    2   7   8   9
    3  17   2  93
    df3
        a  b  c   x  y
    0  11  2  3   2  3
    1   4  5  6  55  6
    2   7  8  9   8  9




    df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=True,add_new_rows=True)

    df1
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    df2
        a   x   y
    0  11   2   3
    1   4  55   6
    2   7   8   9
    3  17   2  93
    df3
        a    b    c   x   y
    0  11  2.0  3.0   2   3
    1   4  5.0  6.0  55   6
    2   7  8.0  9.0   8   9
    3  17  NaN  NaN   2  93




    df1.ds_update(forupdate=df2,update_existing_values=False, add_new_columns=True,add_new_rows=True)

    df1
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    df2
        a   x   y
    0  11   2   3
    1   4  55   6
    2   7   8   9
    3  17   2  93
    df3
        a    b    c   x   y
    0   1  2.0  3.0   2   3
    1   4  5.0  6.0  55   6
    2   7  8.0  9.0   8   9
    3  17  NaN  NaN   2  93

        Parameters:
            df: Union[pd.Series, pd.DataFrame]
            forupdate: Union[pd.Series, pd.DataFrame]
            update_existing_values:bool
                (default=True)
            add_new_columns=True
                (default=True)
            add_new_rows=True
                (default=True)

        Returns:
            Union[pd.Series, pd.DataFrame]

    """
    df11, isseries11 = series_to_dataframe(df)
    df22, isseries22 = series_to_dataframe(forupdate)
    toupdate = df11.copy()
    columns_together = list(set(df11.columns.to_list()) & set(df22.columns.to_list()))
    if update_existing_values is True:
        for ini, d1, d2 in zip(range(len(df11.index)), df11.index, df22.index):
            for ini2, df11col in enumerate(df11.columns):
                value1 = df11.at[d1, df11col]
                value2 = None
                try:
                    value2 = df22.at[d1, df11col]
                except Exception:
                    continue
                if (value1 is value2) or (value1 == value2):
                    pass
                else:
                    toupdate.at[d1, df11col] = value2
    if add_new_rows:
        addrows = list(set(df22.index.to_list()) - set(set(df11.index.to_list())))
        if any(addrows):
            toupdate = pd.concat([toupdate, df22[columns_together].loc[addrows]]).copy()
    if add_new_columns:
        addcolumns = list(set(df22.columns.to_list()) - (set(df11.columns.to_list())))
        if any(addcolumns):
            for col in addcolumns:
                toupdate[col] = df22[col][:len(toupdate)].copy()
    if isseries11:
        if len(toupdate.columns) == 1:
            return toupdate[toupdate.columns[0]]
    return toupdate

def pd_add_df_updater():
    DataFrame.ds_update = update_from_other_dataframe
    Series.ds_update = update_from_other_dataframe

# import numpy as np
#
# df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
#                    columns=['a', 'b', 'c'])
# df2 = pd.DataFrame(np.array([[11, 2, 3], [4, 55, 6], [7, 8, 9], [17, 2, 93]]),
#                    columns=['a', 'x', 'y'])
# print('df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=False,add_new_rows=False)')
#
# df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=False,add_new_rows=False)
# print(f'df1\n{df1}\n')
# print(f'\ndf2\n{df2}\n')
# print(f'\ndf3\n{df3}\n')
#
# df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
#                    columns=['a', 'b', 'c'])
# df2 = pd.DataFrame(np.array([[11, 2, 3], [4, 55, 6], [7, 8, 9], [17, 2, 93]]),
#                    columns=['a', 'x', 'y'])
# print('df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=True,add_new_rows=False)')
#
# df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=True,add_new_rows=False)
# print(f'df1\n{df1}\n')
# print(f'\ndf2\n{df2}\n')
# print(f'\ndf3\n{df3}\n')
#
#
# df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
#                    columns=['a', 'b', 'c'])
# df2 = pd.DataFrame(np.array([[11, 2, 3], [4, 55, 6], [7, 8, 9], [17, 2, 93]]),
#                    columns=['a', 'x', 'y'])
#
# print('df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=True,add_new_rows=True)')
#
# df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=True,add_new_rows=True)
# print(f'df1\n{df1}\n')
# print(f'\ndf2\n{df2}\n')
# print(f'\ndf3\n{df3}\n')
#
#
# df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
#                    columns=['a', 'b', 'c'])
# df2 = pd.DataFrame(np.array([[11, 2, 3], [4, 55, 6], [7, 8, 9], [17, 2, 93]]),
#                    columns=['a', 'x', 'y'])
#
# print('df1.ds_update(forupdate=df2,update_existing_values=False, add_new_columns=True,add_new_rows=True)')
# df3=df1.ds_update(forupdate=df2,update_existing_values=False, add_new_columns=True,add_new_rows=True)
# print(f'df1\n{df1}\n')
# print(f'\ndf2\n{df2}\n')
# print(f'\ndf3\n{df3}\n')