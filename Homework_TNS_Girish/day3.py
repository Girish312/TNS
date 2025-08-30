# Write a function to check whether a given string is a pangram (contains all letters of the alphabet).
"""
def isPangram(sentence):
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True

text = input("Enter a sentence: ")
if isPangram(text):
    print("It's a pangram.")
else:
    print("IT's not a pangram.")
"""
# Write a function that takes a sentence and returns the word with the maximum length.
"""
def longestWord(sentence):
    words = sentence.split()
    maxWord = words[0]

    for word in words:
        if len(word) > len(maxWord):
            maxWord = word
    return maxWord

text = input("Enter a sentence: ")
print("Longest word is:", longestWord(text))
"""

# Write a function to count the number of uppercase and lowercase characters in a string.
"""
def countCase(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

text = input("Enter a string: ")
upper_count, lower_count = countCase(text)
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
"""
