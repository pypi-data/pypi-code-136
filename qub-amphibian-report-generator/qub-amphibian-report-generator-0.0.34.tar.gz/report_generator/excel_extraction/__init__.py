"""# Excel Extraction Package.

This is a package intended to help extract data from an excel spreadsheet and insert it into the designed database.

It is made up of the following python modules:
- clean_data.py:  Code used to clean the data of whitespace, quotation marks, etc. It also locates and removes duplicated entries.
- data_structure.py: This module takes the extracted data from the dataset file and structures it to be inserted into the database.
- excel_to_sql.py: The controller of the package. Creates the database, opens the dataset passes data to other modules before inserting data into database.
- tables.py: Creates strings of SQL to build the database before data is inserted.
"""
