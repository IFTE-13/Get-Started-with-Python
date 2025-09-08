# Reversing an array is the operation of rearranging the array elements in the opposite order. 
# There are various methods and approaches to reverse an array in Python including 
# slicing, reverse(), reversed(), and for loop.

import array as arr

# Creating array
numericArray = arr.array('i', [88, 99, 77, 55, 66])
print("Original array:", numericArray)
# Output: array('i', [88, 99, 77, 55, 66])

# 1. Using slicing
revArray = numericArray[::-1]
print("\nReversed array using slicing:", revArray)
# Output: array('i', [66, 55, 77, 99, 88])

# 2. Using reverse() Method
# Since reverse() is a method of list class, we cannot directly use it 
# to reverse an array created through the Python array module. 
# We have to first transfer the contents of an array to a list with tolist() method, 
# then call the reverse() method, and finally convert the list back to an array.

newArray = numericArray.tolist()     # Convert array to list
newArray.reverse()                   # Reverse the list
revArray = arr.array('i')            # Create an empty array
revArray.fromlist(newArray)          # Fill it with the reversed list
print("\nReversed array using reverse() method:", revArray)
# Output: array('i', [66, 55, 77, 99, 88])

# 3. Using reversed() Method
# reversed() returns an iterator that accesses the elements in reverse order.
newArray = list(reversed(numericArray))   # Convert reversed iterator to list
revArray = arr.array('i', newArray)       # Convert list to array
print("\nReversed array using reversed() function:", revArray)
# Output: array('i', [66, 55, 77, 99, 88])

# 4. Using for Loop
b = arr.array('i')
for i in range(len(numericArray) - 1, -1, -1):   # Iterate backwards
    b.append(numericArray[i])
print("\nReversed array using for loop:", b)
# Output: array('i', [66, 55, 77, 99, 88])
