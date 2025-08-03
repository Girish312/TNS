"""
Python sets -

functions -
1. add()
2. update
3. remove
4. discard
5. pop
6. clear
7. intersaction
8. difference
9. insubset
10. insuperset
11. union
"""

s = {1,2,3,4,5}
print(s)
#add
print(s.add(9))
#update
print(s.update([6,7,8]))
#remove
s.remove(1)
print(s)
#discard
s.discard(2)
print(s)
