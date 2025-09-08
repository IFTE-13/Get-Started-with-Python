#Built-in functions are those functions that are pre-defined in the Python interpreter and you don't need to import any module to use them.

text = "Tutorials Point"

print(len(text)) # Prints 15

# ================== Python Built-in Functions Reference ==================

# 1.  aiter()        → Returns an asynchronous iterator for an asynchronous iterable.
# 2.  all()          → Returns True when all elements in iterable are True.
# 3.  anext()        → Returns the next item from the given asynchronous iterator.
# 4.  any()          → Checks if any element of an iterable is True.
# 5.  ascii()        → Returns string containing printable representation.
# 6.  bin()          → Converts integer to binary string.
# 7.  bool()         → Converts a value to Boolean.
# 8.  breakpoint()   → Drops you into the debugger at the call site (calls sys.breakpointhook()).
# 9.  bytearray()    → Returns array of given byte size.
# 10. bytes()        → Returns immutable bytes object.
# 11. callable()     → Checks if the object is callable.
# 12. chr()          → Returns a character (a string) from an integer.
# 13. classmethod()  → Returns class method for given function.
# 14. compile()      → Returns a code object.
# 15. complex()      → Creates a complex number.
# 16. delattr()      → Deletes attribute from the object.
# 17. dict()         → Creates a dictionary.
# 18. dir()          → Returns attributes of object.
# 19. divmod()       → Returns a tuple of quotient and remainder.
# 20. enumerate()    → Returns an enumerate object.
# 21. eval()         → Runs code within program.
# 22. exec()         → Executes dynamically created program.
# 23. filter()       → Constructs iterator from elements which are true.
# 24. float()        → Returns floating point number from number or string.
# 25. format()       → Returns formatted representation of a value.
# 26. frozenset()    → Returns immutable frozenset object.
# 27. getattr()      → Returns value of named attribute of an object.
# 28. globals()      → Returns dictionary of current global symbol table.
# 29. hasattr()      → Returns whether object has named attribute.
# 30. hash()         → Returns hash value of an object.
# 31. help()         → Invokes the built-in help system.
# 32. hex()          → Converts integer to hexadecimal.
# 33. id()           → Returns identity of an object.
# 34. input()        → Reads and returns a line of string.
# 35. int()          → Returns integer from a number or string.
# 36. isinstance()   → Checks if object is an instance of class.
# 37. issubclass()   → Checks if a class is subclass of another class.
# 38. iter()         → Returns an iterator.
# 39. len()          → Returns length of an object.
# 40. list()         → Creates a list in Python.
# 41. locals()       → Returns dictionary of current local symbol table.
# 42. map()          → Applies function and returns an iterator.
# 43. memoryview()   → Returns memory view of an argument.
# 44. next()         → Retrieves next item from the iterator.
# 45. object()       → Creates a featureless object.
# 46. oct()          → Returns the octal representation of an integer.
# 47. open()         → Returns a file object.
# 48. ord()          → Returns an integer of the Unicode character.
# 49. print()        → Prints the given object.
# 50. property()     → Returns the property attribute.
# 51. range()        → Returns a sequence of integers.
# 52. repr()         → Returns a printable representation of the object.
# 53. reversed()     → Returns the reversed iterator of a sequence.
# 54. set()          → Constructs and returns a set.
# 55. setattr()      → Sets the value of an attribute of an object.
# 56. slice()        → Returns a slice object.
# 57. sorted()       → Returns a sorted list from the given iterable.
# 58. staticmethod() → Transforms a method into a static method.
# 59. str()          → Returns the string version of the object.
# 60. super()        → Returns a proxy object of the base class.
# 61. tuple()        → Returns a tuple.
# 62. type()         → Returns the type of the object.
# 63. vars()         → Returns the __dict__ attribute.
# 64. zip()          → Returns an iterator of tuples.
# 65. __import__()   → Function called by the import statement.

# ------------------- Deprecated / Py2 Only -------------------
# 66. unichr() → Converts a Unicode code point to its corresponding character. (Python 2 only)
# 67. long()   → Represents integers of arbitrary size. (Python 2 only)

# ========================================================================


# 1. Python abs() function
# The abs() function returns the absolute value of x, 
# i.e. the positive distance between x and zero.
# Example: abs(-5) → 5

# 2. Python max() function
# The max() function returns the largest of its arguments 
# or largest number from the iterable (list or tuple).
# Example: max(3, 7, 2) → 7

# 3. Python min() function
# The min() function returns the smallest of its arguments, 
# i.e. the value closest to negative infinity, 
# or smallest number from the iterable (list or tuple).
# Example: min(3, 7, 2) → 2

# 4. Python pow() function
# The pow() function returns x raised to y. 
# It is equivalent to x**y. 
# The function has a third optional argument mod. 
# If given, it returns (x**y) % mod.
# Example: pow(2, 3) → 8 ; pow(2, 3, 5) → 3

# 5. Python round() function
# The round() function returns x rounded to n digits 
# from the decimal point. Default is 0 digits.
# Example: round(5.678, 2) → 5.68

# 6. Python sum() function
# The sum() function returns the sum of all numeric items 
# in any iterable (list or tuple). 
# An optional start argument is 0 by default. 
# If given, the numbers in the list are added to start value.
# Example: sum([1, 2, 3], 10) → 16
