# Write a program to take 5 numbers from the user and store them in a tuple, then print the maximum and minimum.
"""
numbers = []

for i in range(5):
    num = int(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)

numbers = tuple(numbers)

max_num = numbers[0]
min_num = numbers[0]

for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("Tuple:", numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
"""

# Given a tuple of integers, write a program to count how many elements are divisible by 3
"""
tuple1 = (3, 6, 7, 9, 12, 14)
count = 0

for num in tuple1:
    if num % 3 == 0:
        count += 1

print("Count of elements divisible by 3:", count)
"""

# Write a program to reverse the contents of a tuple without using reversed().
"""
tuple2 = (1, 2, 3, 4, 5)

reversed_tuple = ()

for i in range(len(tuple2)-1, -1, -1):
    reversed_tuple += (tuple2[i],)

print("Reversed tuple:", reversed_tuple)
"""
