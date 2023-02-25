# Write your solution here
def factorials(n: int):
    my_dictionary = {}
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
        my_dictionary[i] = factorial

    return my_dictionary