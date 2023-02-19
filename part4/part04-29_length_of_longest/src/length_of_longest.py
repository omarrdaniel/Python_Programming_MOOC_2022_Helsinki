# Write your solution here
def length_of_longest(my_list: list):
    temp = len(my_list[1])
    for string in my_list:
        if len(string) > temp:
            temp = len(string)
    return temp        