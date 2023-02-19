# Write your solution here
# Write your solution here
def shortest(my_list: list):
    temp = len(my_list[1])
    string1 = ""
    for string in my_list:
        if len(string) < temp:
            temp = len(string)
            string1 = string
    return string1  