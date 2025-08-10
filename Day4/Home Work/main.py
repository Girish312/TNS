# Write a program to find the difference between the maximum and minimum elements in a list.
"""
numbers = [1, 2, 3, 5, 10]
maxNum = numbers[0]
minNum = numbers[0]

for num in numbers:
    if num > maxNum:
        maxNum = num
    if num < minNum:
        minNum = num

diff= maxNum - minNum
print(f"Difference between max and min is: {diff}")
"""

# Write a program to remove all elements at odd indices from a list.
"""
list1 = [10, 20, 30, 40, 50, 60]
new_list = []

for i in range(len(list1)):
    if i % 2 == 0:
        new_list.append(list1[i])

print(f"List after removing odd indices: {new_list}")
"""

# Write a program that takes a list of integers and prints only the elements that appear exactly once.
"""
list1 = [1,2,2,3,4,4,5]

for num in list1:
    count = 0
    for i in list1:
        if i == num:
            count += 1
    if count == 1:
        print(num)
"""
