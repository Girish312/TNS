# 1. Write a program that converts a list of tuples into a dictionary. 
# Example: [('a', 1), ('b', 2)] → {'a': 1, 'b': 2}
"""
pairs = [('a', 1), ('b', 2), ('c', 3)]
result = {}

for key, value in pairs:
    result[key] = value
print("Dictionary:", result)
"""

# 2. Given a dictionary with values as lists, write a program to flatten all values into a single list.
"""
data = {'fruits': ['apple', 'banana'],
        'colors': ['red', 'blue'],
        'animals': ['cat', 'dog']}
flattened = []

for value_list in data.values():
    for item in value_list:
        flattened.append(item)

print(f"Flattened list: {flattened}" )
"""

# 3. Write a program that takes a list with duplicate elements and returns a dictionary with elements as keys and their frequency as values
"""
list1 = [1, 2, 2, 3, 4, 4, 4, 5]
frequency = {}

for num in list1:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Frequency dictionary:", frequency)
"""
