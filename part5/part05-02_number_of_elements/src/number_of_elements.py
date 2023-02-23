# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in range(len(my_matrix)):
        for column in range(len(my_matrix[row])):
            if my_matrix[row][column] == element:
                count +=1
    return count