# Write your solution here
def times_ten(start_index: int, end_index: int):
    diz = {}
    for i in range(start_index,end_index+1):
        diz[i] = i*10
    return diz
