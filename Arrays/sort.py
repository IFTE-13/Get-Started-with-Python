# The array class doesn't have any function/method to give a sorted arrangement 
# of its elements. However, we can achieve it with one of the following approaches −
# 1. Using a sorting algorithm (manual implementation)
# 2. Using the sort() method from List
# 3. Using the built-in sorted() function

import array as arr

# Original array
a = arr.array('i', [10, 5, 15, 4, 6, 20, 9])
print("Original array:", a)
# Output: array('i', [10, 5, 15, 4, 6, 20, 9])

# -----------------------------
# 1. Bubble Sort Algorithm (Manual Sorting)
# -----------------------------
ascArray = arr.array('i', a)  # copy for ascending
for i in range(len(ascArray)):
    for j in range(i + 1, len(ascArray)):
        if ascArray[i] > ascArray[j]:
            ascArray[i], ascArray[j] = ascArray[j], ascArray[i]
print("\nArray after bubble sort (ascending):", ascArray)
# Output: array('i', [4, 5, 6, 9, 10, 15, 20])

descArray = arr.array('i', a)  # copy for descending
for i in range(len(descArray)):
    for j in range(i + 1, len(descArray)):
        if descArray[i] < descArray[j]:
            descArray[i], descArray[j] = descArray[j], descArray[i]
print("Array after bubble sort (descending):", descArray)
# Output: array('i', [20, 15, 10, 9, 6, 5, 4])

# -----------------------------
# 2. Using sort() Method
# -----------------------------
sortedList = a.tolist()
sortedList.sort()  # ascending
sortedArray = arr.array('i', sortedList)
print("\nArray after using sort() method (ascending):", sortedArray)
# Output: array('i', [4, 5, 6, 9, 10, 15, 20])

sortedList = a.tolist()
sortedList.sort(reverse=True)  # descending
sortedArray = arr.array('i', sortedList)
print("Array after using sort() method (descending):", sortedArray)
# Output: array('i', [20, 15, 10, 9, 6, 5, 4])

# -----------------------------
# 3. Using sorted() Function
# -----------------------------
sortedArray2 = arr.array('i', sorted(a))  # ascending
print("\nArray after using sorted() function (ascending):", sortedArray2)
# Output: array('i', [4, 5, 6, 9, 10, 15, 20])

sortedArray2 = arr.array('i', sorted(a, reverse=True))  # descending
print("Array after using sorted() function (descending):", sortedArray2)
# Output: array('i', [20, 15, 10, 9, 6, 5, 4])


# Note:
# i.   Bubble Sort (manual) – Good for learning, not efficient for large arrays.
# ii.  list.sort() – Sorts a list in place; needs conversion between array ↔ list.
# iii. sorted() – Returns a new sorted list; convert back to array if needed.
# iv.  All methods support descending order (either by reversing manually, reverse=True, or flipping comparison in bubble sort).