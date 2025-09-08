# Numbers types
# Python supports three types of numbers
# 1. int - Integer (whole numbers) e.g., 1, 2, 3, -5
# 2. float - Floating point numbers (decimal numbers) e.g., 1.5, -0.75, 3.14
# 3. complex - Complex numbers e.g., 2 + 3j, -1 + 4j

# Integer Numbers
a = 10
b = 20
c = a + b

print ("a:", a, "type:", type(a)) # a : 10 type: <class 'int'>
print ("a:", a, "type:", type(b)) # b : 20 type: <class 'int'>
print ("c:", c, "type:", type(c)) # c : 30 type: <class 'int'>

# Binary, Octal and Hexadecimal Numbers
x = 0b1010  # Binary representation of 10
y = 0o24    # Octal representation of 20
z = 0x1E    # Hexadecimal representation of 30
print ("x:", x, "type:", type(x)) # x : 10 type: <class 'int'>
print ("y:", y, "type:", type(y)) # y : 20 type: <class 'int'>
print ("z:", z, "type:", type(z)) # z : 30 type: <class 'int'>

# Note: Binary, Octal and Hexadecimal numbers are also of type 'int' in Python.

# Note: Big integers (integers larger than 32 or 64 bits) are supported in Python and can be created by simply assigning a large value to a variable.
big_int = 1234567890123456789012345678901234567890
print("big_int:", big_int, "type:", type(big_int)) # big_int: 1234567890123456789012345678901234567890 type: <class 'int'>

# Floating Point Numbers
p = 10.5
q = 20.75
r = p + q
print ("p:", p, "type:", type(p)) # p : 10.5 type: <class 'float'>
print ("q:", q, "type:", type(q)) # q : 20.75 type: <class 'float'>
print ("r:", r, "type:", type(r)) # r : 31.25 type: <class 'float'>
# Note: Floating point numbers are represented in double precision (64-bit) in Python.
# You can use the float() function to convert an integer to a floating point number.

# Complex Numbers
m = 2 + 3j
n = 1 + 4j
o = m + n
print ("m:", m, "type:", type(m)) # m : (2+3j) type: <class 'complex'>
print ("n:", n, "type:", type(n)) # n : (1+4j) type: <class 'complex'>
print ("o:", o, "type:", type(o)) # o : (3+7j) type: <class 'complex'>
# Note: Complex numbers are represented as a pair of floating point numbers (real and imaginary parts) in Python.
# You can use the complex() function to create a complex number from two floats.
# You can access the real and imaginary parts of a complex number using the .real and .imag attributes.
print("Real part of m:", m.real) # Real part of m: 2.0
print("Imaginary part of m:", m.imag) # Imaginary part of m: 3.0
# You can also use the abs() function to get the magnitude of a complex number.
print("Magnitude of m:", abs(m)) # Magnitude of m: 3.605551275463989

