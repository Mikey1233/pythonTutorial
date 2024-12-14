#write a factorial function

def factorial (num) : 
 if type(num) != int : 
     return None
 if num < 0 : 
     return None
 if num == 0 :
     return 1
 return num * factorial(num - 1)

result = factorial(5)
print(result)
print(type(4.5) ==  int)

class Dog :
    def __init__ (self,name) :
        self.name = name
dog = Dog("biily")
print(type(dog))
