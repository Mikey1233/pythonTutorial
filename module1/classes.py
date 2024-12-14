#Classes and Objects
class Cat :
    def __init__(self ,name) :
        self.name = name
        self.legs = 4
    def speak(self) :
        print(self.name + " says " + "Meow" )
myCat = Cat("milly")
myCat.speak()