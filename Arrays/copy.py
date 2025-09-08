import array as arr
import copy

# Creating array
a = arr.array('i', [110, 220, 330, 440, 550])
print("Original array:", a)  
# Output: array('i', [110, 220, 330, 440, 550])

# 1. Assignment Operator (shallow copy)
b = a
print("\nCopied array using assignment operator:", b)
# Output: array('i', [110, 220, 330, 440, 550])
print("Memory address of a:", id(a))
print("Memory address of b:", id(b))
# Both ids will be the same → b is just a reference to a

# 2. Deep Copy
c = copy.deepcopy(a)
print("\nCopied array using deepcopy:", c)
# Output: array('i', [110, 220, 330, 440, 550])
print("Memory address of c:", id(c))
# Different id → independent copy of a
