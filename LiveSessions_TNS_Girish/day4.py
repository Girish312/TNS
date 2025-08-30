"""
#Append the number 100 in the list
number = [10,20,30,40,50,60,70]
number.append(100)
print(number)

#insert the number 50 at the 3rd position
number = [10,20,30,40,60,70]
number.insert(2,50)
print(number)

#remove the first occurence of the number 20
number = [10,20,30,40,50,60,70]
number.remove(20)
print(number)

#count how many times 10 appears in the list
number = [10,20,30,40,50,60,70,10,10]
print(number.count(10))

#reverse the list
number = [10,20,30,40,50,60,70]
number.reverse()
print(number)

#sort the list in an ascending order
number = [10,20,30,40,50,60,70]
number.sort()
print(number)
number1 = [1,2,3,4,5,6,7,8,9]
number1.sort(reverse = True)
print(number1)

#find the maximum and minimum values in the list
number = [10,20,30,40,50,60,70]
print(max(number))
print(min(number))
list1 = ["Amit", "Zatch", "pappu"] #it will print Min as A and max as Z
print(max(list1))
print(min(list1))

#calculate the sum of all elements in the list
number = [10,20,30,40,50,60,70]
print(sum(number))

#given a tuple of number and a targeted element, find and print all indexes where the targeted element occurs in the tuple
number = (1,2,3,4,5,6,7,8,9,10,5,11,5)
targeted_element = 5
for index in range(len(number)):
    if number[index] == targeted_element:
        print(index)
        
"""