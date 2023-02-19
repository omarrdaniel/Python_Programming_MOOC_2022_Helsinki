# Write your solution here
list = []
while True:
    n = int(input("Number"))
    if n == 0:
        print("Bye!")
        break
    list.append(n)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")