from glist import Gcsv


gcsv = None
def write_sheet(spreadsheet_id: str, sheet: (int, str), data: list):
    """

    Args:
        - spreadsheet_id (str): Get this from the URL of the Google Sheet.
        - sheet (int, str): A sheet name or index starting at 0 (this is a tab in the spreadsheet).
        - data (list): The rows to write at the sheet.

    Returns:
        - success (bool)
    """
    global gcsv
    if gcsv is None:
        gcsv = Gcsv()
    gcsv.write(spreadsheet_id, sheets=[sheet], data=data)
    return True
