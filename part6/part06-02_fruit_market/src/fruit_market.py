# write your solution here
def read_fruits():
    diz = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.replace("\n","")
            fruit = line.split(";")
            diz[fruit[0]] = float(fruit[1])
    return diz