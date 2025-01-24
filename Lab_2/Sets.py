#Python Sets
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Access Set Items
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Add Set Items
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove Set Items
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)