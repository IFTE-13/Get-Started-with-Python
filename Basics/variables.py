# invalid rules
# -> 123name = "wrong"   # cannot start with digit
# -> user-name = "bad"   # hyphen not allowed
# -> class = "oops"      # keyword not allowed

# valid rules
name = "IFTEKHAR"
_age = 19
user123 = "student"

# Note:
# Can contain letters, numbers, and _
# Cannot start with a number
# Case-sensitive (age ≠ Age)
# Cannot use reserved keywords (for, class, etc.)

# Variable assignment
x = 10 # single assignment
a, b = 5, 15  # multiple assignment
c = d = 20    # same value assignment

# Types of Variables
integer_var = 100          # Integer
float_var = 10.5           # Float
string_var = "Hello"       # String
boolean_var = True         # Boolean
# Note: Check types using type() function (e.g., type(integer_var))

# Local vs Global Variables
global_var = "I am global"  # Global variable
def my_function():
    local_var = "I am local"  # Local variable
    print(local_var)          # Accessible here
    print(global_var)         # Accessible here
    global global_var2        # Declare global variable inside function which is accassible outside
    global_var2 = "I am also global"

# print(local_var)  # Error: Not accessible here
print(global_var2) # Accessible here
my_function()

# Variable Types (Based on Data)
# Numbers → int, float, complex
# Sequence → str, list, tuple, range
# Mapping → dict
# Set Types → set, frozenset
# Boolean → True, False
# Binary → bytes, bytearray, memoryview

# Special Variable Types
x = None # NoneType or represents absence of value
PI = 3.14159 # Constant (by convention, uppercase name)
# __name__, __file__, __init__ these are special variables (dunder variables)

# Memory Management
x = 10
print(id(x))  # prints memory address of x

# Shared References
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] because both point to same list

# Variable Annotations (Python 3.6+)
name: str = "Iftekahr"
age: int = 20
height: float = 5.9

print(name, age, height) # Iftekahr 20 5.9

# Deleting Variables
x = 10
del x   # deletes variable x
# print(x)  # Error: x is deleted