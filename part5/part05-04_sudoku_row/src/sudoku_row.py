# Write your solution here
def row_correct(sudoku : list, row_index : int):
    new_list = []
    for i in range(0, 9):
        sudoku[row_index][i]
        if sudoku[row_index][i] > 0 and  sudoku[row_index][i] in new_list:
            return False
        else:
            new_list.append(sudoku[row_index][i])
    return True