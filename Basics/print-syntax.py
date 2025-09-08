print ("Hello, World!") # Hello, World!

print ("Hello", "World", 123, True) # Hello World 123 True

# using sep and end parameters
print("A", "B", "C", sep="-")    # A-B-C
print("Hello", end="")           # no newline
print("World")                   # continues same line (e.g., HelloWorld)

# string formatting
name = "IFTEKHAR"
print(f"Hello, {name}")          # Hello, IFTEKHAR (available in Python 3.6+)
print("Hello, {}".format(name))  # Hello, IFTEKHAR
print("Hello, %s" % name)        # Hello, IFTEKHAR (old style)

# using modules
import sys #importing at the beginning of the file is a good practice
sys.stdout.write("Hello, World!\n")  # Hello, World!

import os
os.write(1, b"Hello World\n")  # Hello, World! (works on Unix-like systems)

import logging
logging.warning("Hello, World!")  # WARNING:root:Hello, World!

__builtins__.print("Hello from builtins")

# advanced ways
## pretty print
from pprint import pprint
pprint({"name": "IFTEKHAR", "age": 30, "city": "New York", "skills": ["Python", "C++", "JavaScript"]})
pprint({"b": 1, "a": [1,2,3]}) # {'a': [1, 2, 3], 'b': 
# Note: pprint prints dict in sorted order by keys

## json dump
import json
print(json.dumps({"a":1, "b":2}, indent=2)) 
print(json.dumps({"b":1, "a":2}, indent=2)) # keys are not sorted

# variable to hold print output
x = "Hello\nWorld"
print(x)  # prints with newline
print(repr(x))  # prints with escape characters 'Hello\nWorld'
print(str(x))   # prints with newline Hello
