# You can remove element of an array using remove() and pop() methods.
import array as arr

# Creating an integer array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
print("Initial array:", numericArray)  
# Output: array('i', [111, 211, 311, 411, 511])

# 1. remove(value) → Removes the first occurrence of the specified value
numericArray.remove(311)
print("After remove(311):", numericArray)  
# Output: array('i', [111, 211, 411, 511])

# 2. pop(index) → Removes element at the given index
numericArray.pop(3)   # removes element at index 3 (511)
print("After pop(3):", numericArray)  
# Output: array('i', [111, 211, 411])
