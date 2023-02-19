# Write your solution here
def greatest_number(x,y,z):
    array = [x,y,z]
    return max(array)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(9, -1, 3)
    print(greatest)