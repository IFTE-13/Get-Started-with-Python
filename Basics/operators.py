# operators are special symbols used to perform specific operations
# they can be arithmetic, comparison, logical, bitwise, assignment, identity, and membership operators
# there are three types of operators in Python:
# 1. Unary operators: operate on a single operand  
# 2. Binary operators: operate on two operands
# 3. Ternary operators: operate on three operands (conditional expression)

# Arithmetic Operators
a = 10  
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division
print("Floor Division:", a // b)   # Floor Division
print("Modulus:", a % b)           # Modulus
print("Exponentiation:", a ** b)   # Exponentiation

# Comparison Operators
print("Comparison Operators:")
print("Equal to:", a == b)          # Equal to
print("Not equal to:", a != b)      # Not equal to
print("Greater than:", a > b)       # Greater than
print("Less than:", a < b)          # Less than
print("Greater than or equal to:", a >= b)  # Greater than or equal to
print("Less than or equal to:", a <= b)     # Less than or equal to

# Logical Operators
x = True
y = False
print("Logical Operators:")
print("Logical AND:", x and y)      # Logical AND
print("Logical OR:", x or y)        # Logical OR
print("Logical NOT:", not x)         # Logical NOT

# Bitwise Operators
c = 5  # In binary: 0101
d = 3  # In binary: 0011
print("Bitwise Operators:")
print("Bitwise AND:", c & d)        # Bitwise AND
print("Bitwise OR:", c | d)         # Bitwise OR
print("Bitwise XOR:", c ^ d)        # Bitwise XOR
print("Bitwise NOT:", ~c)           # Bitwise NOT
print("Left Shift:", c << 1)        # Left Shift
print("Right Shift:", c >> 1)       # Right Shift

# Assignment Operators
e = 10
print("Assignment Operators:")
e += 5  # Equivalent to e = e + 5
print("e after += 5:", e)
e -= 3  # Equivalent to e = e - 3
print("e after -= 3:", e)
e *= 2  # Equivalent to e = e * 2
print("e after *= 2:", e)
e /= 4  # Equivalent to e = e / 4
print("e after /= 4:", e)
e %= 3  # Equivalent to e = e % 3
print("e after %= 3:", e)
e **= 2 # Equivalent to e = e ** 2
print("e after **= 2:", e)
e //= 2 # Equivalent to e = e // 2
print("e after //= 2:", e)

# Identity Operators
f = [1, 2, 3]   
g = f
h = [1, 2, 3]
print("Identity Operators:")
print("f is g:", f is g)           # True, because g references the same object as f
print("f is h:", f is h)           # False, because h is a different object
print("f is not h:", f is not h)   # True, because f and
print("f is not g:", f is not g)   # False, because f and g reference the same object g
print("f == h:", f == h)           # True, because f and h have the same content
print("f != h:", f != h)           # False, because f and h have the same content
print("f == g:", f == g)           # True, because f and g reference the same object
print("f != g:", f != g)           # False, because f and g reference the same object
print("g is h:", g is h)           # False, because g and h are different objects
print("g is not h:", g is not h)   # True, because g and h are different objects
print("g == h:", g == h)           # True, because g and h have the same content
print("g != h:", g != h)           # False, because g and h have the same content
print("g is f:", g is f)           # True, because g references the same object as f
print("g is not f:", g is not f)   # False, because g references the same object as f

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("3 in my_list:", 3 in my_list)        # True, because 3 is in my_list
print("6 in my_list:", 6 in my_list)        # False, because
print("3 not in my_list:", 3 not in my_list) # False, because 3 is in my_list
print("6 not in my_list:", 6 not in my_list) # True, because 6 is not in my_list 6 is not in my_list

# Ternary Operator (Conditional Expression)
age = 18
status = "Adult" if age >= 18 else "Minor"
print("Ternary Operator:")
print("Status:", status)  # Output: Adult
# The ternary operator is a shorthand for an if-else statement
# It evaluates the condition (age >= 18) and returns "Adult" if True, otherwise returns "Minor" 
# It is useful for simple conditional assignments
# Note: Python does not have a dedicated ternary operator like some other languages, but the conditional expression serves the same purpose


