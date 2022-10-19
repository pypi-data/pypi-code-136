from contextlib import contextmanager
from openpyxl import load_workbook
from pandas import ExcelWriter

def df_update_join(df_1, df_2):
    """Joins `df_1` to `df_2` by adding columns if they don't exist or replacing columns if they do.

    Args:
        df_1 (DataFrame): Original dataframe
        df_2 (DataFrame): Dataframe with columns to add or replace

    Returns:
        DataFrame: Updated dataframe with new or updated columns
    """
    df = df_1.drop(df_1.columns.intersection(df_2.columns), axis=1).join(df_2)
    return df

@contextmanager
def dfs_to_excel(output_filepath, df_dict):
    """Saves a list of dfs to excel utilizing openpyxl.
    Args:
        output_filepath (str or unicode): Filepath of workbook to save to.
        df_dict (dict): Dictionary of dataframes to save to Excel.
            (key, value) pairs should be in the form of (Excel sheet name, df)
    """
    try:
        wb = load_workbook(output_filepath)
        writer = ExcelWriter(output_filepath, engine='openpyxl')
        writer.book = wb
        writer.sheets = dict((ws.title, ws) for ws in wb.worksheets)

        for sheet_name, df in df_dict.items():
            df.to_excel(writer, sheet_name)
    finally:
        wb.save(output_filepath)
    