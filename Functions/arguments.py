# default arguments
def greet(name, msg="Hello!"):
    print(name + ', ' + msg)
    
greet("Alice")          # uses default msg
greet("Bob", "Hi!")     # overrides default msg

# Mutable default arguments
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst
print(append_to_list(1)) # [1]
print(append_to_list(2)) # [1, 2]
print(append_to_list(3)) # [1, 2, 3]
print(append_to_list(4, [5, 6])) # [5, 6, 4]

# Keyword arguments
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet(pet_name='Willie') # uses default animal_type
describe_pet(pet_name='Harry', animal_type='hamster') # overrides default animal_type   

# Note: In keyword arguments, the order of arguments does not matter

# In user defined method
def func(a, b=2, c=3):
    print(f"a: {a}, b: {b}, c: {c}")
func(1)          # a=1, b=2, c=3
func(1, 4)       # a=1, b=4, c=3
func(1, 4, 5)    # a=1, b=4, c=5

def intr(amt, *, rate):
   val = amt*rate/100
   return val
   
interest = intr(1000, rate=10)
print(interest)

# Note: putting a * in the function definition forces the use of keyword arguments for parameters after *

# Positional-only parameters (Python 3.8+)
def pos_only(a, b, /, c, d):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
pos_only(1, 2, c=3, d=4)    # a=1, b=2, c=3, d=4   
pos_only(1, b=2, c=3, d=4)  # Error: b must be positional
pos_only(1, 2, 3, 4)        # Error: c and d can be keyword or positional

# Note: putting a / in the function definition forces the use of positional arguments for parameters before /

# Positional-only
def add(a, b, /):
    return a + b
print(add(2, 3))  # works
# print(add(a=2, b=3))  # Error
# print(add(2, b=3))    # Error
# print(add(a=2, 3))    # Error

# Arbitrary arguments
# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s

result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)

# Note: *args allows passing a variable number of non-keyword arguments to a function. 

# Arbitrary keyword arguments
def person(name, **kwargs):
    print("Name:", name)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
person("Alice", age=30, city="New York")
person("Bob", job="Engineer")

# Note: **kwargs allows passing a variable number of keyword arguments to a function.

# Combining different types of arguments
def func(a, b=2, *args, c=3, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, c: {c}, kwargs: {kwargs}")
func(1)                            # a=1, b=2, args=(), c=3, kwargs={}
func(1, 4)                         # a=1, b=4, args=
func(1, 4, 5, 6, c=7, d=8, e=9)    # a=1, b=4, args=(5,6), c=7, kwargs={'d':8,'e':9}    
# Note: The order of parameters must be: positional-only, standard, *args, keyword-only, **kwargs

# Required arguments
#avg of first test and best of following tests
def avg(first, *rest):
   second=max(rest)
   return (first+second)/2
   
result=avg(40,30,50,25)
print (result)

# Optional arguments
def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
result=percent(math=80, sci=75)
print ("percentage:", result)
