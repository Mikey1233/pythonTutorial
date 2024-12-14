print("hello world!")
print("first time writing python")
y = 20
# print(type(y))
# type(y)

print(4j + 7j)
print("hello " + "world")
# print(1.0001 == 1.0)

# Python Data Structure
# List
my_list = [1,2,3,4]
my_list2 = [2,34,5]
my_list2.append(45)
print(my_list2)
# print(len(my_list2))

# sets

my_set = {1,2,1,4}
my_set.add(6)
print(my_set)

#Tupple
my_tuple = (98,99,100)
print(my_tuple)
# Why use Tuples ?
#They're are memory efficient
#Good for storing lots of little things like x,y coordinates

# Dictionaries
my_dictionary = {
    "apple" : "A red fruit",
    "Iphone" : "A smart phone"
}
my_dictionary["rat"] = "A small animal"
print(my_dictionary)
print(my_dictionary["apple"])
# Sets and Dictionaries Similarities
# Both are defined with curly brackets
# Sets have unique values,dictionaries have unique keys
# The order doesn't matter