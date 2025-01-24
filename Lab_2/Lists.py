#python list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Access List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Change List Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Lists
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

#Sort Lists
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Join Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
