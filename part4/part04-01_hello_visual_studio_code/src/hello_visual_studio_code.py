# Write your solution here
while True:
    string = input("Editor:")
    if string.lower() == "word" or string.lower() == "notepad":
        print("awful")
    elif string.lower() != "visual studio code":
        print("not good")
    elif string.lower() == "visual studio code":
        print("an excellent choiche!")
        break
