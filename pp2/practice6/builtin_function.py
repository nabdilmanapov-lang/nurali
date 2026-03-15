#Return the absolute value of a number:
x = abs(-7.25)

#Check if all items are True:
mylist = [True, True, True]
x = all(mylist)
mytuple = (0, True, False)
x = all(mytuple)
myset = {0, 1, 0}
x = all(myset)
mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)

from functools import reduce
# Use map() on lists
# Squares each number
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# Use filter() on lists
# Gets even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Aggregate with reduce()
# Multiplies all numbers together
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

# Use enumerate()
# Prints index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Use zip() for paired iteration
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)

# Type checking
x = 10

print("Type of x:", type(x))

if isinstance(x, int):
    print("x is an integer")

# Type conversions
# String to integer
a = int("5")

# Integer to float
b = float(10)

# Number to string
c = str(25)

print(a, b, c)
