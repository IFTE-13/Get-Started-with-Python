# Python does not have a built-in array data type (like C or Java).
# Instead, the "array" module is available, which provides a way to store
# multiple elements of the same data type efficiently.
#
# Key Points:
# - An array holds elements of the same data type.
# - Indexing starts at 0 (zero).
# - Syntax: array_name = array(typecode, [initializer])
# - typecode: A single character that specifies the type of array elements.
# - initializer: (optional) List or iterable used to initialize the array.

import array as arr

# Creating an integer array
arr1 = arr.array("i", [1, 2, 3])

# Display type and contents
print("Type of arr1:", type(arr1))
print("Contents of arr1:", arr1)
