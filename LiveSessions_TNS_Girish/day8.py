# 1. write a python function to check whether a given number is a prime number or not.
"""
def primenum(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print (primenum(0))
"""

# 2. given a list of integers write a function to return a new list containing only the even numbers from the original list
"""
def evenNum (list1):
    newList = []
    for num in list1:
        if num % 2 == 0:
            newList.append(num)
    return newList
    
print(evenNum([2,4,3,2,5,8,4,9]))
"""

# 3. write a python code to find the second largest number in the list without using any built in sort function
"""
def checkSecondLargest(num):
  Largest = 0
  second_largest= 0
  for i in range(0, len(num)):
    if num[i] > Largest:
      second_largest = Largest
      Largest = num[i]
    elif num[i] > second_largest:
      second_largest = num[i]
  print(second_largest)
checkSecondLargest([1,2,3,4,5,6,7,9,8])
"""

# 4. given a list of tuples, write a function that returns a list of tuple sorted based on the second element in each tuple.
"""
def sortBySecondElement(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])
print(sortBySecondElement([(1, 3), (2, 2), (3, 1)]))
"""

# 5. write a python function that take a tuples of number and return a sum of all elements
"""
def sum_of_tuple(my_tuple):
    total = 0
    for num in my_tuple:
        total += num
    return total

numbers = (1, 2, 3, 4)
print(sum_of_tuple(numbers))
"""

# 6. given two list write a function to return common elements using set operations
"""
def common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(common(a, b))
"""

# 7. write a python program to remove all the duplicates from the list using a set & return a unique element from the list
"""
def remove_duplicates(my_list):
    unique_set = set(my_list)
    return list(unique_set)

nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))
"""

# 8. write a python function that takes a dictionary and returns a key with maximum value
"""
def maxKey(my_dict):
    max_key = None
    max_value = 0

    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

data = {"a": 10, "b": 25, "c": 15}
print(maxKey(data))
"""

# 9. write a python program to count the frequency of each character in a given string using a dictionary
"""
def charfreq(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

word = "banana"
print(charfreq(word))
"""

# 10.given a list of student names and their marks in a dictionary, 
# write a function to return the name() of the student with high remarks
def scholarstudent(student_dict):
    highest = 0
    for marks in student_dict.values():
        if marks > highest:
            highest = marks

    top_students = []
    for name, marks in student_dict.items():
        if marks == highest:
            top_students.append(name)

    return top_students

students = {"Girish": 85, "Kartik": 92, "Yash": 92, "Devesh": 88}
print(scholarstudent(students))
