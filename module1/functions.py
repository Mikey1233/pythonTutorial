#Functions

def multiplyByTwo(val) :
    return val * 2
result = multiplyByTwo(4)

def squareOfInput(val) :
    return val * val

result2 = squareOfInput(9)
print(result)
print(result2)

#functions without the return value
def appendItemToList(List,item) : 
        List.append(item)
myList = [1,2,4]
appendItemToList(myList,3)

print(myList)