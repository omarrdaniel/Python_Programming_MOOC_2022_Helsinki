# Write your solution here
def all_the_longest(my_list):

    longest = 0
    newList = []

    for i in my_list:
        if len(i) > longest:
            longest = len(i)

    for i in my_list:
        if len(i) == longest:
            newList.append(i)

    return newList