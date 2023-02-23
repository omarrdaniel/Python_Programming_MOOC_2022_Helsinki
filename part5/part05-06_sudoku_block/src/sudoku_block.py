# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list = []
    for row in range(row_no, row_no+3):
        for element in range(column_no, column_no+3):
            number = sudoku[row][element]
            if number > 0 and number in new_list:
                return False
            new_list.append(number)
 
    return True