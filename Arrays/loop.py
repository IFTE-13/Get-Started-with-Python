import array as arr

# Creating an array
newArray = arr.array('i', [56, 42, 23, 85, 45])
print("Initial array:", newArray)  
# Output: array('i', [56, 42, 23, 85, 45])

# 1. Using for loop
print("\nIterating using for loop:")
for iterate in newArray:
    print(iterate)
# Output:
# 56
# 42
# 23
# 85
# 45

# 2. Using while loop
print("\nIterating using while loop:")
idx = 0
while idx < len(newArray):
    print(newArray[idx])
    idx += 1
# Output:
# 56
# 42
# 23
# 85
# 45
