# Write your solution here
def no_shouting(my_list: list) -> list:
    new_list = []
    for string in my_list:
        if not string.isupper():
            new_list.append(string)
    return new_list