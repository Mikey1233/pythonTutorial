#Lists in Depth

myList = list(range(100))

print(myList[::-20])
# modifying list

myList2 = [1,2,3]
myList2.append(4)
myList2.insert(3,8)
print(myList2)
myList2.pop()
numOf2 = myList2.count(2)
print(myList2)
print(numOf2)