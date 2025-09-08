import array as arr
import copy

# -----------------------------
# 1. Creating an array
# -----------------------------
a = arr.array('i', [1, 2, 3])
print("Original array:", a)  
# Output: array('i', [1, 2, 3])

# -----------------------------
# 2. Accessing items
# -----------------------------
print("Access index 0:", a[0])          # Output: 1
print("Slicing [0:2]:", a[0:2])        # Output: array('i', [1,2])

# -----------------------------
# 3. Iteration
# -----------------------------
print("\nIteration using for loop:")
for item in a:
    print(item)
# Output: 1 2 3

print("\nIteration using while loop:")
idx = 0
while idx < len(a):
    print(a[idx])
    idx += 1
# Output: 1 2 3

# -----------------------------
# 4. Adding/Modifying Items
# -----------------------------
a.append(4)
print("\nAfter append(4):", a)         # Output: array('i', [1,2,3,4])

a.insert(1, 10)
print("After insert(1,10):", a)        # Output: array('i', [1,10,2,3,4])

b = arr.array('i', [5,6])
a.extend(b)
print("After extend([5,6]):", a)       # Output: array('i', [1,10,2,3,4,5,6])

# -----------------------------
# 5. Removing Items
# -----------------------------
a.remove(10)
print("\nAfter remove(10):", a)        # Output: array('i', [1,2,3,4,5,6])

popped_value = a.pop(2)
print("After pop(2):", a)              # Output: array('i', [1,2,4,5,6])
print("Popped value:", popped_value)   # Output: 3

a.clear()
print("After clear():", a)             # Output: array('i', [])

# -----------------------------
# 6. Copying arrays
# -----------------------------
a = arr.array('i', [1,2,3])
b = a                # Assignment (shallow copy)
c = copy.deepcopy(a) # Deep copy
print("\nOriginal a:", a)  
print("Shallow copy b:", b)
print("Deep copy c:", c)
print("id(a)==id(b):", id(a)==id(b))   # True
print("id(a)==id(c):", id(a)==id(c))   # False

# -----------------------------
# 7. Reversing arrays
# -----------------------------
numericArray = arr.array('i', [10,20,30,40,50])

# Using slicing
rev1 = numericArray[::-1]
print("\nReversed using slicing:", rev1)  # Output: array('i', [50,40,30,20,10])

# Using reverse() method via list and fromlist()
temp_list = numericArray.tolist()
temp_list.reverse()
rev2 = arr.array('i')
rev2.fromlist(temp_list)
print("Reversed using reverse() method:", rev2)  # Output: array('i', [50,40,30,20,10])

# Using reversed() function
rev3 = arr.array('i', list(reversed(numericArray)))
print("Reversed using reversed() function:", rev3)  # Output: array('i', [50,40,30,20,10])

# Using for loop
rev4 = arr.array('i')
for i in range(len(numericArray)-1, -1, -1):
    rev4.append(numericArray[i])
print("Reversed using for loop:", rev4)  # Output: array('i', [50,40,30,20,10])

# -----------------------------
# 8. Sorting arrays
# -----------------------------
a = arr.array('i', [10,5,15,4,6,20,9])

# Bubble sort ascending
ascArray = arr.array('i', a)
for i in range(len(ascArray)):
    for j in range(i+1, len(ascArray)):
        if ascArray[i] > ascArray[j]:
            ascArray[i], ascArray[j] = ascArray[j], ascArray[i]
print("\nBubble sort ascending:", ascArray)  # Output: array('i', [4,5,6,9,10,15,20])

# Bubble sort descending
descArray = arr.array('i', a)
for i in range(len(descArray)):
    for j in range(i+1, len(descArray)):
        if descArray[i] < descArray[j]:
            descArray[i], descArray[j] = descArray[j], descArray[i]
print("Bubble sort descending:", descArray)  # Output: array('i', [20,15,10,9,6,5,4])

# Using sort() method via list
sortedList = a.tolist()
sortedList.sort()
sortedArray = arr.array('i', sortedList)
print("Sort() ascending:", sortedArray)  # Output: array('i', [4,5,6,9,10,15,20])

sortedList = a.tolist()
sortedList.sort(reverse=True)
sortedArray = arr.array('i', sortedList)
print("Sort() descending:", sortedArray)  # Output: array('i', [20,15,10,9,6,5,4])

# Using sorted() function
sortedArray2 = arr.array('i', sorted(a))
print("Sorted() ascending:", sortedArray2)  # Output: array('i', [4,5,6,9,10,15,20])

sortedArray2 = arr.array('i', sorted(a, reverse=True))
print("Sorted() descending:", sortedArray2)  # Output: array('i', [20,15,10,9,6,5,4])

# -----------------------------
# 9. Merging arrays
# -----------------------------
a = arr.array('i', [1,2,3])
b = arr.array('i', [4,5,6])

# Using append()
for i in range(len(b)):
    a.append(b[i])
print("\nMerge using append():", a)  # Output: array('i', [1,2,3,4,5,6])

# Using + operator
a = arr.array('i', [1,2,3])
b = arr.array('i', [4,5,6])
mergedList = a.tolist() + b.tolist()
a = arr.array('i', mergedList)
print("Merge using + operator:", a)    # Output: array('i', [1,2,3,4,5,6])

# Using extend()
a = arr.array('i', [1,2,3])
b = arr.array('i', [4,5,6])
a.extend(b)
print("Merge using extend():", a)      # Output: array('i', [1,2,3,4,5,6])
