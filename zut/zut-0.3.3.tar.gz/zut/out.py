from __future__ import annotations
import os, sys, csv, locale
from pathlib import Path
from io import IOBase

# Register CSV dialect for French version of Excel
class ExcelFr(csv.excel):
    delimiter = ";"

csv.register_dialect('excel-fr', ExcelFr())

class open_out:
    """
    ## Usage examples
    
    ### Export text either on stdout or on csv file

    ```
    with open_out(filename or "stdout") as o:
        o.file.write("10: Zidane")
    ```
    
    ### Export tabular data either on stdout or on csv file

    ```
    with open_out(filename or "stdout") as o:
        o.append_headers("Id", "Name")
        o.append_row(10, "Zidane")
    ```
    """
    file: IOBase

    def __init__(self, out: str|Path|IOBase = None, append: bool = False, newline: str = None, encoding: str = None, csv_dialect: str = None, **kwargs):
        self._append = append
        self._newline = newline
        self._encoding = encoding
        self._csv_dialect = csv_dialect

        # Update out
        self._opened = False
        self.file: IOBase = None
        self._strpath: str = None
        if out != "noop":
            if not out or out == "stdout":
                self.file = sys.stdout
            elif out == "stderr":
                self.file = sys.stderr
            elif isinstance(out, IOBase):
                self.file = out
            elif isinstance(out, Path):
                self._strpath = str(out)
            elif isinstance(out, str):
                self._strpath = out
            else:
                raise AttributeError(f"out: invalid type {type(out).__name__}")

        # For CSV file:
        # - Set newline to '', otherwise newlines embedded inside quoted fields will not be interpreted correctly. See footnote of: https://docs.python.org/3/library/csv.html
        # - Set encoding to utf-8-sig (UTF8 with BOM): CSV is for exchanges, encoding should not depend on the exporting operating system. BOM is necessary for correct display with Excel
        if (self._strpath and self._strpath.lower().endswith(".csv")) or self._csv_dialect:
            if self._newline is None:
                self._newline = ''
            if self._encoding is None:
                self._encoding = 'utf-8-sig'

        # Handle strpath
        if self._strpath:
            # Replace "{key}" in path by keyword arguments
            for key, value in kwargs.items():
                self._strpath = self._strpath.replace("{"+key+"}", value)
        elif self.file:
            if hasattr(self.file, "name"):
                self._strpath = self.file.name
            if not self._strpath:
                self._strpath = f"<{type(self.file).__name__}>"

    def __enter__(self):
        if not self.file and self._strpath:
            self._opened = True
            Path(self._strpath).parent.mkdir(parents=True, exist_ok=True)
            self.file = open(self._strpath, "a" if self._append else "w", newline=self._newline, encoding=self._encoding)
        return self

    def __exit__(self, *args):
        if self.file:
            if self._opened:
                self.file.close()
            elif self.headers or self.rows:
                from tabulate import tabulate
                print(tabulate(self.rows, headers=self.headers), file=self.file)

    def __str__(self) -> str:
        if self._strpath:
            return self._strpath
        else:
            return "<noop>"

    # -------------------------------------------------------------------------
    # For tabular data
    # -------------------------------------------------------------------------

    @property
    def headers(self):
        if not hasattr(self, "_headers"):
            return None
        return self._headers
    
    def append_headers(self, *args):
        data = args[0] if len(args) == 1 and isinstance(args[0], list) else args
        self._headers = data
        if self._opened:
            self.csv_writer.writerow(data)
        # else: will be handled in exit method by tabulate

    @property
    def rows(self):
        if not hasattr(self, "_rows"):
            self._rows = []
        return self._rows

    def append_row(self, *args):
        data = args[0] if len(args) == 1 and isinstance(args[0], list) else args
        self.rows.append(data)
        if self._opened:
            self.csv_writer.writerow(data)
        # else: will be handled in exit method by tabulate

    @property
    def csv_writer(self):
        if not hasattr(self, "_csv_writer"):
            dialect = os.environ.get("CSV_DIALECT", self._csv_dialect)
            if not dialect:
                loc = locale.getdefaultlocale()
                if loc[0].startswith("fr"):
                    dialect = "excel-fr"
                else:
                    dialect = "excel"
            self._csv_writer = csv.writer(self.file, dialect=dialect)
        return self._csv_writer
