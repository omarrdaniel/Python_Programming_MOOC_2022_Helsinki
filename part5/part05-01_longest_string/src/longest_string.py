# Write your solution here
def longest(strings: list):
    longest = strings[0]
    for word in strings:
        if len(longest) < len(word):
            longest = word
    return longest