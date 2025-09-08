# You can add elements to an array using append(), insert(), and extend() methods.

import array as arr

# Creating an integer array
a = arr.array('i', [1, 2, 3])
print("Initial array:", a)   # Output: array('i', [1, 2, 3])

# 1. append() → Adds an element at the end of the array
a.append(10)
print("After append(10):", a)   # Output: array('i', [1, 2, 3, 10])

# 2. insert() → Inserts an element at a specific index
a.insert(1, 20)  
print("After insert(1, 20):", a)   # Output: array('i', [1, 20, 2, 3, 10])

# 3. extend() → Adds elements from another array
b = arr.array('i', [6, 7, 8, 9, 10])
a.extend(b)
print("After extend(b):", a)  
# Output: array('i', [1, 20, 2, 3, 10, 6, 7, 8, 9, 10])