# Write your solution here
def no_vowels(string: str):
    i = 0
    vowel = ['a','e','i','o','u']
    for c in string:
        if c in vowel:
            string = string.replace(c,"")
        i+=1
    return string
