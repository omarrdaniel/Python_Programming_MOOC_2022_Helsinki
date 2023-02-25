# Write your solution here
def create_tuple(x: int, y: int, z: int):
    my_list = [x,y,z]
    smallest = min(my_list)
    greatest = max(my_list)
    somma = sum(my_list)

    return (smallest,greatest,somma)

    