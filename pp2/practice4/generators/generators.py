def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

def simple_gen():
  yield 1
  yield 2

# This will raise StopIteration
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) 

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

#The send() method allows you to send a value to the generator:
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) 
gen.send("Hello")
gen.send("World")

#The close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
