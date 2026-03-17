from functools import reduce
# Use map() on lists
# Squares each number
def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))

# Use filter() on lists
# Gets even numbers
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)

# Aggregate with reduce()
# Multiplies all numbers together
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

# Use enumerate()
# Prints index and value
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

# Use zip() for paired iteration
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(a, b)

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
