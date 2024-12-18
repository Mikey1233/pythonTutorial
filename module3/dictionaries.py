from collections import defaultdict
petStore = {
     "shiro" : "dog",
     "billy" : "pig",
     "dunk" : "cow"
 }

print(petStore["shiro"])

petStore['dunk'] = "elephant"

print(petStore)

keys = list(petStore.keys())
values = list(petStore.values())
print(keys)
print(values)

print(petStore.get("shio"))
length = len(petStore)


animals = defaultdict(list)

animals['a'].append('ant')
print(animals)

# List compprehension
newList = list((1,2,3,4))
newList2 = [2 * item for item in newList]
print(newList2)

filteredList = [item for item in newList if item % 2 == 0]
print(filteredList)

# Dictionary comprehension
zooList = [["a","ant"],["b","bear"],['c','cat'],["d","dog"]]

zoo = {item[0] : item[1] for item in zooList}
zoo2 = {key:value for key,value in zooList}

zooListItems = list(zoo.items())
zoo3 = [{"letter":key,"animalname":value} for key,value in zooListItems]

print(zoo)
print(zoo2)
print(zoo3)

