# List is mutable in Python
# the contents of list can be modified in place, after the object is stored in the memory.
# list1[i] = newvalue

# Change Consecutive Items
list1 = ["a", "b", "c", "d"]

print ("Original list: ", list1)

list2 = ['Y', 'Z']
list1[1:3] = list2

print ("List after changing with sublist: ", list1)

# Change a Range of Items
# If the source sublist has more items than the slice to be replaced, the extra items in the source will be inserted.
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['X','Y', 'Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)

# If the sublist with which a slice of original list is to be replaced, has lesser items, the items with match will be replaced and rest of the items in original list will be removed.
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)

