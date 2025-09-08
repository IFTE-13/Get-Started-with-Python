# The process of joining two arrays is termed as merging or concatenating.
# Python provides multiple ways to merge two arrays such as append(), + operator, and extend() methods.
# Note: Both arrays must be of the same data type; otherwise, an error will occur.

import array as arr

# Creating two arrays
a = arr.array('i', [10, 5, 15, 4, 6, 20, 9])
b = arr.array('i', [2, 7, 8, 11, 3, 10])
print("Array a:", a)  # Output: array('i', [10, 5, 15, 4, 6, 20, 9])
print("Array b:", b)  # Output: array('i', [2, 7, 8, 11, 3, 10])

# 1. Using append() method (append each element of b to a)
for i in range(len(b)):
    a.append(b[i])
print("\nArray after merging using append():", a)
# Output: array('i', [10, 5, 15, 4, 6, 20, 9, 2, 7, 8, 11, 3, 10])

# Reset array a for next method
a = arr.array('i', [10, 5, 15, 4, 6, 20, 9])

# 2. Using + operator (convert to list, add, and convert back to array)
x = a.tolist()
y = b.tolist()
z = x + y
a = arr.array('i', z)
print("\nArray after merging using + operator:", a)
# Output: array('i', [10, 5, 15, 4, 6, 20, 9, 2, 7, 8, 11, 3, 10])

# Reset array a for next method
a = arr.array('i', [10, 5, 15, 4, 6, 20, 9])

# 3. Using extend() method
a.extend(b)
print("\nArray after merging using extend():", a)
# Output: array('i', [10, 5, 15, 4, 6, 20, 9, 2, 7, 8, 11, 3, 10])
