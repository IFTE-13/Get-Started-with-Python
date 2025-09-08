# function is a block of organized, reusable code that is used to perform a single, related action.
# Functions provide better modularity for your application and a high degree of code reusing.
# You can define functions to provide the required functionality

# Type of Functions
# 1. Built-in functions
# 2. User-defined functions
# 3. Anonymous functions (Lambda functions)

# Syntax to define a function
def hello(name):
    print("Hello, " + name)
    
hello("Alice")

# python uses pass by reference, so if you change a mutable object within a function, the changes are reflected outside the function
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)

# Function with default parameters
def greet(name, msg="Good morning!"):   
    print("Hello", name + ', ' + msg)
greet("Bob")
greet("Bob", "How do you do?")

# Anonymous functions (Lambda functions)
square = lambda x: x * x
print("Square of 5:", square(5))
# A function can have zero or more parameters
