# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as new_file:
        new_file.write(person[0]+";"+str(person[1])+";"+str(person[2])+"\n")
