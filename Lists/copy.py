# Shallow Copy
# A shallow copy in Python creates a new object, but instead of copying the elements recursively, it copies only the references to the original elements. This means that the new object is a separate entity from the original one, but if the elements themselves are mutable, changes made to those elements in the new object will affect the original object as well.

import copy
# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a shallow copy
shallow_copied_list = copy.copy(original_list)
# Modifying an element in the shallow copied list
shallow_copied_list[0][0] = 100
# Printing both lists
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

# Deep Copy
# A deep copy in Python creates a completely new object and recursively copies all the objects referenced by the original object. This means that even nested objects within the original object are duplicated, resulting in a fully independent copy where changes made to the copied object do not affect the original object, and vice versa.
import copy
# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a deep copy
deep_copied_list = copy.deepcopy(original_list)
# Modifying an element in the deep copied list
deep_copied_list[0][0] = 100
# Printing both lists
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

# Slice Notation
# [start:end:step]
# Any modifications made to the copied list will not affect the original list, and vice versa, because they are separate objects in memory.
# Original list
original_list = [1, 2, 3, 4, 5]
# Copying the list using slice notation
copied_list = original_list[1:4]
# Modifying the copied list
copied_list[0] = 100
# Printing both lists
print("Original List:", original_list)
print("Copied List:", copied_list)

# list() Function
# The list() function in Python is a built-in function used to create a new list object. It can accept an iterable (like another list, tuple, set, etc.) as an argument and create a new list containing the elements of that iterable. If no argument is provided, an empty list is created.
# Original list
original_list = [1, 2, 3, 4, 5]
# Copying the list using the list() constructor
copied_list = list(original_list)
# Printing both lists
print("Original List:", original_list)
print("Copied List:", copied_list)

# copy() Function
# the copy() function is used to create a shallow copy of a list or other mutable objects. This function is part of the copy module in Python's standard library.
import copy
original_list = [1, 2, 3, 4, 5]
# Copying the list using the copy() function
copied_list = copy.copy(original_list)
print("Copied List:", copied_list)


# Key Differences (Copy vs List Function)
# Feature	     |  list()	                                  |  copy()
# ---------------|--------------------------------------------|------------------------------
# Works on	     |  Any iterable (string, tuple, set…)	      |  Only on lists
# Purpose	     |  Convert/construct a new list	          |  Copy an # existing list
# Copy type	     |  Creates a new list (shallow copy if       |  list given)	Shallow copy
# Nested objects |	Still shared (not deep)	Still             |  shared (not deep)