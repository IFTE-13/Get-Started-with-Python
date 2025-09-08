# Numeric Types
x = 10          # integers - unlimited size
y = 3.14        # float - double precision
z = 1 + 2j      # complex - real and imaginary parts

# Sequence Types
s = "Hello"     # string - immutable sequence of characters
nums = [1, 2, 3]  # list - mutable sequence of items
t = (1, 2, 3)   # tuple - immutable sequence of items
r = range(5)    # range - immutable sequence of numbers (e.g., 0 to 4)
r = range(1, 10, 2)  # range with start, stop, step (e.g., 1, 3, 5, 7, 9)

# Mapping Type
d = {"name": "Alice", "age": 25}  # dictionary - key-value pairs (mutable)

# Set Types
s = {1, 2, 3}   # set - unordered collection of unique items (mutable)
fs = frozenset([1, 2, 3])  # frozenset - immutable version of set
# Note: Sets do not allow duplicate values
# Example: s = {1, 2, 2, 3} results in s = {1, 2, 3}

# Boolean Type
is_active = True  # boolean - True or False

# Binary Types
b = b"Hello"     # bytes - immutable sequence of bytes 
ba = bytearray(b"Hello")  # bytearray - mutable sequence of bytes
mv = memoryview(b"Hello")  # memoryview - memory view of bytes

# Special Type
n = None         # NoneType - represents absence of value or null value

# Type Checking
print(type(x))         # <class 'int'> 
print(type(s))         # <class 'str'>
print(type(d))         # <class 'dict'>
print(type(is_active)) # <class 'bool'>
print(type(b))         # <class 'bytes'>
print(type(n))         # <class 'NoneType'>
# Use isinstance() for type checking
print(isinstance(x, int))  # True

# Collections Module (Extra Data Types)
from collections import Counter
print(Counter("BANANA"))  # Counter({'A': 3, 'N': 2, 'B': 1})

# Dynamic Typing
var = 10        # var is an integer
print(var, type(var))  # 10 <class 'int'>
var = "Hello"   # var is now a string
print(var, type(var))  # Hello <class 'str'>
# Note : Python is dynamically typed, so variable types can change. Python cares about behavior or valur, not type.

# Duck Typing
class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"
def animal_sound(animal):
    print(animal.speak())   # Works for any object with a speak() method
dog = Dog() 
cat = Cat()
animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!

def add(x, y):
    return x + y

print(add(5, 10))       # works
print(add("Hi", "Yo"))  # also works