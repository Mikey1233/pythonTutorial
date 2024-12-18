myset = {'a','b','c'}
print(myset)

myset2 = set({'d','e','f'})
myset2.add('g')
print(myset2)

print('g' in myset2)
print('g' in myset)
myset2.pop()

myset2.discard('e')
print(len(myset2))

# Tuppple

mytuple = ('a','b','c')
print(mytuple[0])

def returnMultipleVal() :
    return 1,2,3

ans = type(returnMultipleVal())
a,b,c = returnMultipleVal()
print(ans,a,b,c)

