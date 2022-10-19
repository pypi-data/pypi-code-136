def csudoku(data):
  sudoku_size = len(data[0])

  for line in range(sudoku_size):
    local_array_column = []
    for column in range(sudoku_size):
      try:
        local_array_column.append(data[column][line])
      except:
        print("[Error] the condition is not met NxN")
        return False
  if sudoku_size != len(local_array_column):
    return False

  ideal_array = []
  for i in range(sudoku_size):
    ideal_array.append(i+1)

  Success = True

  blocks_sudoku = []
  blocks_size = int(sudoku_size ** 0.5)

  def check_block(shift_pos_line, shift_pos_column, data0):
    timeout_array = []
    for stroka in range(blocks_size): # возьмем первые n строки
      first_elements = 0
      for nomer in range(blocks_size):
        if first_elements < blocks_size:
          timeout_array.append(data0[stroka + shift_pos_column][nomer + shift_pos_line])
        else:
          break
        first_elements += 1
    blocks_sudoku.append(timeout_array)

  for column in range(0, blocks_size*blocks_size, blocks_size):
    for line in range(0, blocks_size*blocks_size, blocks_size):
      try:
        check_block(line, column, data)
      except:
        return False

  for column in range(sudoku_size):
    local_array_line = []
    for line in range(sudoku_size):
      local_array_line.append(data[column][line])
    local_array_line.sort()

    if local_array_line != ideal_array:
      print("[Error] " + str(local_array_line))
      return False

  for line in range(sudoku_size):
    local_array_column = []
    for column in range(sudoku_size):
      local_array_column.append(data[column][line])
    local_array_column.sort()

    if local_array_column != ideal_array:
      print("[Error] " + str(local_array_column))
      return False

  return Success