# Write your solution here
def sum_of_positives(my_list: list):
    sum = 0
    for n in my_list:
        if n>0:
            sum += n
    return sum