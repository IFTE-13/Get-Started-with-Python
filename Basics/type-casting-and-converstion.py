# Implicit Type Conversion (Type Promition)
x = 5       # int
y = 2.0     # float
result = x + y  # int is converted to float
print(result)  # Output: 7.0
print(type(result))  # Output: <class 'float'>

# Note: Python automatically converts a smaller data type into a larger one to prevent data loss. This is safe and automatic.

# Explicit Type Conversion (Type Casting)
a = 10      # int
b = 3.5     # float
# Converting float to int (explicitly)
c = int(b)  # float to int
print(c)    # Output: 3
print(type(c))  # Output: <class 'int'>

a = "100"
b = int(a)  # str to int
print(b + 50)  # Output: 150
print(type(b))  # Output: <class 'int'>
# Note: Explicit conversion is done by the programmer to convert one data type to another. This may lead to data loss if not handled properly.

# Casting vs Conversion — Same or Different?
# In Python, the terms "casting" and "conversion" are often used interchangeably. Both refer to the process of changing an object's data type.
# Every casting is a form of conversion, but not every conversion is casting.
# Conversion = Changing data type (implicit or explicit)
# Casting = Explicitly changing data type (explicit)

# Unsafe Type Casting
x = "Hello"
y = int(x)  # This will raise a ValueError: invalid literal for int() with base 10: 'Hello'
print(y)  # Uncommenting the above lines will cause an error

float("xyz")   # ValueError
dict([1,2,3])  # TypeError (needs key-value pairs)

# Loss of precision
f = 9.99
i = int(f)  # f is converted to 9, fractional part is lost

# String parsing rules
int("123abc")  # ValueError
float("12.34.56")  # ValueError
complex("1+2j3")  # ValueError
print(int("0b101", 2))  # binary string to int → 5
# Example: 
# bool("True")  # True, but bool("False") is also True because non-empty strings are True
# bool("")  # False
# bool("0")  # True, because non-empty strings are True
# bool(" ")  # True, because non-empty strings are True
# bool("None")  # True, because non-empty strings are True
# bool(None)  # False
# bool([])  # False
# bool([0])  # True, because non-empty lists are True
# bool({})  # False
# bool({0: "zero"})  # True, because non-empty dicts are True
# bool(())  # False
# bool((0,))  # True, because non-empty tuples are True
# bool(set())  # False
# bool({0})  # True, because non-empty sets are True
# bool(frozenset())  # False
# bool(frozenset([0]))  # True, because non-empty frozensets are True
# bool(bytearray())  # False    
# bool(bytearray(b'0'))  # True, because non-empty bytearrays are True
# bool(bytes())  # False
# bool(bytes(b'0'))  # True, because non-empty bytes are True
# bool(memoryview(b''))  # False
# bool(memoryview(b'0'))  # True, because non-empty memoryviews are True
# bool(range(0))  # False
# bool(range(1))  # True, because non-empty ranges are True
# bool(complex(0, 0))  # False
# bool(complex(1, 0))  # True, because non-zero complex numbers
# bool(complex(0, 1))  # True, because non-zero complex numbers
# bool(complex(1, 1))  # True, because non-zero complex numbers
# bool(float('nan'))  # True, because NaN is considered a non-zero float
# bool(float('inf'))  # True, because infinity is considered a non-zero float
# bool(float('-inf'))  # True, because negative infinity is considered a non-zero float
# bool(int('0'))  # False
# bool(int('1'))  # True, because non-zero integers are True
# bool(int('-1'))  # True, because non-zero integers are True
# bool(int('100'))  # True, because non-zero integers are True
# bool(int('-100'))  # True, because non-zero integers are True
# bool(int('000'))  # False
# bool(int('001'))  # True, because non-zero integers are True
# bool(int('-001'))  # True, because non-zero integers are True

# Demo:
class MyNumber:
    def __init__(self, value):
        self.value = value
    def __int__(self):
        return int(self.value)

n = MyNumber(42.7)
print(int(n))   # 42