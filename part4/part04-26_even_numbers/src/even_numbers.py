# Write your solution here
def even_numbers(my_list: list) -> list:
    new_list = []
    for n in my_list:
        if n%2==0:
            new_list.append(n)
    return new_list
