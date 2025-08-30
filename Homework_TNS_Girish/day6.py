# Write a program to take two lists from the user and print the common elements using sets.
"""
list1 = []
list2 = []

n1 = int(input("How many elements in first list? "))
for i in range(n1):
    list1.append(int(input("Enter element for list 1: ")))

n2 = int(input("How many elements in second list? "))
for i in range(n2):
    list2.append(int(input("Enter element for list 2: ")))

set1 = set(list1)
set2 = set(list2)
common = set1 & set2

print("Common elements:", common)
"""

# Write a program to check if two sets are disjoint or not.
"""
set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("Sets are disjoint.")
else:
    print("Sets are NOT disjoint.")
"""

# Write a program to find all unique vowels present in a given string using set.
"""
text = input("Enter a string: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}

foundVowels = set()

for ch in text:
    if ch in vowels:
        foundVowels.add(ch)

print("Unique vowels found:", foundVowels)
"""