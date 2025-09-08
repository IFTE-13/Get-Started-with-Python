# Accessing an array means retrieving values stored at specific indices.
# Indexing starts from 0, just like lists.

import array as arr

# Creating an integer array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
print("Array:", numericArray)   # Output: array('i', [111, 211, 311, 411, 511])

# 1. Indexing
print(numericArray[0])   # Output: 111
print(numericArray[1])   # Output: 211
print(numericArray[2])   # Output: 311

# 2. Iteration using a for loop
for item in numericArray:
    print(item)  
# Output:
# 111
# 211
# 311
# 411
# 511

# 3. Iteration using enumerate()
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, Value: {val}")
# Output:
# Index: 0, Value: 111
# Index: 1, Value: 211
# Index: 2, Value: 311
# Index: 3, Value: 411
# Index: 4, Value: 511

# 4. Slicing operations
print(numericArray[2:])    # Output: array('i', [311, 411, 511])
print(numericArray[0:3])   # Output: array('i', [111, 211, 311])
