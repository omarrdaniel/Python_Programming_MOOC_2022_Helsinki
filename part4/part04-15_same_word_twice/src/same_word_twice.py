# Write your solution here
list = []
i = 0
while True:
    word = input("Type a word:")
    if word in list:
        print(f"You typed in {len(list)} different words")
        break
    list.append(word)
