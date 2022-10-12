# Script for reading and writing from Google Spreadsheets as with csv's
import os
import argparse
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GSheet(gspread.models.Worksheet):
  def __init__(self, worksheet, gcsv, sheet_index=0):
    type(self).__new__(worksheet.__class__)
    self.__dict__.update(worksheet.__dict__)
    self.gcsv = gcsv
    self.data = []
    self.updated_cells = []
    self.index = sheet_index
  
  # Returns data as lists of lists
  #  and also stores in self.data
  # Set return_formulas to true to return formulas instead of output values,
  #  where applicable
  def read(self, return_formulas=True, params={}):
#     self.data = self.get_all_values() # Doesn't allow parameters
#     if return_formulas:
    if return_formulas:
      params['valueRenderOption'] = 'FORMULA'
    self.data = self.spreadsheet.values_get(self.title, params)
    try:
      self.data = gspread.utils.fill_gaps(self.data['values'])
    except KeyError:
      self.data = []
    return self.data
  
  # filetype can also be 'tsv' for tab separation
  def download(self, directory='', filename='', filetype='csv'):
    if not self.data:
      self.read(return_formulas=False)
    if not filename:
      filename = self.title + '.' + filetype
    filename = os.path.join(directory, filename)
    delim = ','
    if filetype == 'tsv':
      delim = '\t'
    with open(filename, 'w') as file:
      writer = csv.writer(file, delimiter=delim)
      for row in self.data:
          writer.writerow(row)
    
    return filename
  
  # Write data to this sheet
  #   will overwrite previous values
  # Data is lists of lists
  # If data is not provided, will use self.data
  # send_formulas=True sets ValueInputOption to USERENTERED, which means
  #  input is formatted and used as it would be when entered manually
  def write(self, data=None, old_data=None, force=True, send_formulas=True):
    if not force:
      return self.populate(data, old_data)
    if not data:
      data = self.data
    new_cells = data_to_cells(data)

    if len(new_cells) > 0:
      if send_formulas:
        input_option = "USER_ENTERED"
      else:
        input_option = "RAW"
      self.update_cells(new_cells, value_input_option=input_option) # Send all cells
  
  # Populate this sheet with new data for empty cells
  #   will not overwrite previous values
  # Data is lists of lists
  # If data is not provided, will use self.data
  # If old_data is provided, this function won't request
  #   the whole sheet again to verify that no data is overwritten
  def populate(self, data, old_data=None):
    if not data:
      if self.data:
        data = self.data
      else:
        data = self.read()
        old_data = data
    if not old_data:
      old_data = self.read(return_formulas=False) # Have refs to empty cells be empty
    new_cells = data_to_populated_cells(data, old_data)
    if len(new_cells) > 0:
      self.update_cells(new_cells) # Send all cells

  # sheet_identifier may be a title, index, or id
  def is_sheet(self, sheet_identifier):
    if sheet_identifier == self.title or sheet_identifier == self.index or sheet_identifier == self.id:
      return True
    return False

  def copy(self):
    return self.__copy__()
  
  def __copy__(self):
    obj = type(self).__new__(self.__class__)
    obj.__dict__.update(self.__dict__)
    return obj


# data is a matrix (lists of lists) of values
def data_to_cells(data):
  cells = []
  for row_i in range(len(data)):
    row = data[row_i]
    if not isinstance(row, list): # For example, if the data is already a list of cells
      return data
    
    for col_i in range(len(row)):
      cell = gspread.models.Cell(row_i+1, col_i+1, row[col_i]) # row an col start at 1
      cells.append(cell)
  return cells

# data is a matrix (lists of lists) of values
def data_to_populated_cells(data, old_data):
  cells = []
  for row_i in range(len(data)):
    row = data[row_i]
    for col_i in range(len(row)):
      old_val = None
      do_update = False
      new_val = row[col_i]
      if not old_data or not len(old_data) or row_i >= len(old_data) or \
          (col_i > 0 and not isinstance(old_data[0], list)) or col_i >= len(old_data[row_i]):
        do_update = True
      else:
        old_val = old_data[row_i][col_i]
        if old_val is None or old_val == '':
          do_update = True

      if do_update and new_val is not None and new_val != '':
        cell = gspread.models.Cell(row_i+1, col_i+1, new_val) # row an col start at 1
        cells.append(cell)
  return cells


# Read and write to Google Spreadsheets as if they're csv files, then batch update all changes.
class Gcsv:
  # Authorize Google Sheets API
  # key_filename should be a json file provided by Google
  def __init__(self, key_filename=None):
    scope = ['https://spreadsheets.google.com/feeds']
    if not key_filename:
      try:
        key_filename = os.environ['GOOGLE_APPLICATION_CREDENTIALS'] # env variable with filename
      except KeyError:
        print("Either provide the credential key filename (JSON file) or set GOOGLE_APPLICATION_CREDENTIALS environment variable with the filename")
        exit()
    self.credentials = ServiceAccountCredentials.from_json_keyfile_name(key_filename, scope)
    self.spread = gspread.authorize(self.credentials)
  
  # Returns all sheets in a spreadsheet, or specific sheets
  # sheets may be the name of a sheet, or the index
  def open(self, id, sheets=None):
    spreadsheet = self.spread.open_by_key(id)
    worksheets = spreadsheet.worksheets()
    chosen_sheets = []
    chosen_indexes = []
    if sheets is not None and not isinstance(sheets, list):
      sheets = [sheets]
    if sheets:
      sheet_index = 0
      for sheet in sheets:
        if isinstance(sheet, str): # sheet is a title
          worksheet = spreadsheet.worksheet(sheet)
          chosen_sheet = GSheet(worksheet, self, sheet_index)
        else:
          if sheet > len(worksheets): # sheet is a gid
            sheet_index_j = 0
            for worksheet in worksheets: # Not particularly efficient if there are many worksheets
              if sheet == worksheet.id:
                chosen_sheet = GSheet(worksheet, self, sheet_index_j)
                break
              sheet_index_j += 1
          else: # sheet is an index in the spreadsheet
            worksheet = worksheets[sheet]
            chosen_sheet = GSheet(worksheet, self, sheet_index)
        if not chosen_sheet:
          print("Sheet "+str(sheet)+" not found")
        if chosen_sheet:
          chosen_sheets.append(chosen_sheet)
        sheet_index += 1
    else:
      chosen_sheets = worksheets
      for worksheet_i in range(len(chosen_sheets)):
        # Convert to GSheet
        chosen_sheets[worksheet_i] = GSheet(chosen_sheets[worksheet_i], self, worksheet_i)
    if len(chosen_sheets) == 1:
      # Don't return as a list if there's only one (common case)
      chosen_sheets = chosen_sheets[0]
    return chosen_sheets
  
  # Return list of lists for a specific sheet,
  # or for multiple sheets
  # Set return_formulas to true to return formulas instead of output values,
  #  where applicable
  def read(self, id, sheets=None, return_formulas=False, params={}):
    sheets_data = []
    chosen_sheets = self.open(id, sheets)
    if not isinstance(chosen_sheets, list):
      chosen_sheets = [chosen_sheets]
    for worksheet in chosen_sheets:
      sheets_data.append(worksheet.read(return_formulas=return_formulas, params=params))
    if len(sheets_data) == 1:
      return sheets_data[0]
    return sheets_data
    
  # Save specific sheet(s) as a csv
  # Returns filenames where sheets were written
  # filetype can also be 'tsv' for tab separation
  # Set return_formulas to true to return formulas instead of output values,
  #  where applicable
  def download(self, id, sheets=None, directory='', filetype='csv',
               force=True, return_formulas=False, params={}, verbose=True):
    worksheets = self.open(id, sheets)
    filenames = []
    delim = ','
    if filetype == 'tsv':
      delim = '\t'
    if not isinstance(worksheets, list):
      worksheets = [worksheets]
    for worksheet in worksheets:
      filename = os.path.join(directory, worksheet.title) + '.' + filetype
      filenames.append(filename)
      data = worksheet.read(return_formulas=return_formulas, params=params)
      if os.path.isfile(filename):
        # Only download cells that were empty locally
        # Do this by filling in GSheet data with any additions from the local csv
        with open(filename, 'r') as file:
          reader = csv.reader(file)
          row_i = 0
          for row in reader:
            # If GSheet doesn't have this row, add a new one
            if row_i >= len(data):
              data.append(row)
            else:
              data_row = data[row_i]
              for col_i in range(len(row)):
                cell_val = row[col_i]
                
                if col_i >= len(data_row):
                  data_row.append(cell_val)
                else:
                  data_cell = data_row[col_i]
                  if force and (data_cell is None or data_cell == ''):
                    # Only use local value is cell is empty
                    data[row_i][col_i] = cell_val
                  elif not force and not (cell_val is None or cell_val == ''):
                    # Always use local_value, if not empty
                    data[row_i][col_i] = cell_val
            row_i += 1
      with open(filename, 'w') as file:
        writer = csv.writer(file, delimiter=delim)
        for row in data:
            writer.writerow(row)
        if verbose:
          print("Downloaded "+filename)
    return filenames
  
  # Write data to specific sheets
  # Data is lists of lists, one for each 
  #   sheet specified
  # send_formulas sets ValueInputOption to USERENTERED, which means
  #  input is formatted and used as it would be when entered manually
  def write(self, id, sheets, data, old_data=None, force=True, 
           send_formulas=True):
    worksheets = self.open(id, sheets)
    if not isinstance(worksheets, list):
      worksheets = [worksheets]
    if not isinstance(sheets, list):
      sheets = [sheets]
      data = [data]
    try:
      if not isinstance(data[len(sheets)-1][0], list):
        data = [data]
    except (KeyError, IndexError, TypeError):
      pass
    if not force:
      if not old_data:
        old_data = self.read(id, sheets, return_formulas=False) # Have refs to empty cells be empty
      elif not isinstance(old_data, list):
        old_data = [old_data]
      try:
        if not isinstance(old_data[len(sheets)-1][0], list):
          old_data = [old_data]
      except (KeyError, TypeError, IndexError):
        print("Invalid old data")
        exit()
    for sheet_i in range(len(worksheets)):
      worksheet = worksheets[sheet_i]
      if not worksheet:
        continue
      sheet_data = None
      # Handle cases where a sheet wasn't found, altering the ordering of worksheets
      # This shouldn't be necessary, because open appends None in such cases
      if not worksheet.is_sheet(sheets[sheet_i]):
        for sheet_j in range(len(sheets)):
          if worksheet.is_sheet(sheets[sheet_j]):
            sheet_data = data[sheet_j]
      else:
        sheet_data = data[sheet_i]
#       if force:
#         new_cells = data_to_cells(data[sheet_i])
#       else:
#         new_cells = data_to_populated_cells(data[sheet_i], old_data[sheet_i])
#       if len(new_cells) > 0:
        if not force:
          old_data_sheet = old_data[sheet_i]
        else:
          old_data_sheet = None
        return worksheet.write(data[sheet_i], old_data_sheet, force=force, 
                               send_formulas=send_formulas) # Send all cells
  
  # Like write, but only update cells that were empty 
  # If old_data is provided, this function won't request
  #   the whole sheet again to verify that no data is overwritten
  def populate(self, id, sheets, data, old_data=None, force=False, 
           send_formulas=True):
    return self.write(id, sheets, data, old_data, force, send_formulas=send_formulas)
