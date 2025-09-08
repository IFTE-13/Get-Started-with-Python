# Removing list items in Python implies deleting elements from an existing list. When we remove list items, we are reducing the size of the list or eliminating specific elements.

# pop() Method
# The pop() method is used to removes and returns the last element from a list if no index is specified, or removes and returns the element at a specified index, altering the original list.
list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop()
print ("List after popping: ", list2)
list2.pop(2)
print ("List after popping: ", list2)

# remove() Method
# The remove() method is used to remove the first occurrence of a specified item from a list.
list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)
list1.remove("Physics")
print ("List after removing: ", list1)

# clear() Method
# The clear() method is used to remove all elements from a list, leaving it empty.
my_list = [1, 2, 3, 4, 5]
# Clearing the list
my_list.clear()
print("Cleared list:", my_list)

# del Keyword
# The del keyword is used to delete element either at a specific index or a slice of indices from memory.
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)

# deleting a series of consecutive items
list2 = [25.50, True, -55, 1+2j]
print ("List before deleting: ", list2)
del list2[0:2]
print ("List after deleting: ", list2)