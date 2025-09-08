# formatting in Python is the process of building a string representation dynamically by inserting the value of numeric expressions in an already existing string.

# % operator
name = "World"
print("Welcome to %s!" % name)

# format() method
str = "Welcome to {}"
print(str.format("World"))

# f-strings (formatted string literals)
item1_price = 2500
item2_price = 300
total = f'Total: {item1_price + item2_price}'
print(total)

# Template strings
from string import Template

# Defining template string
str = "Hello and Welcome to $name !"

# Creating Template object
templateObj = Template(str)

# now provide values
new_str = templateObj.substitute(name="World")
print(new_str)


