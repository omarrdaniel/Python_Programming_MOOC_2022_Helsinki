# Write your solution here
def everything_reversed(my_list: list) -> list:
    new_list = []
    for string in my_list:
        new_list.append(string[::-1])
    new_list.reverse()
    return new_list