#Python Tuples
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Access Tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Update Tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Unpack Tuples
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#loop Tuples
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)