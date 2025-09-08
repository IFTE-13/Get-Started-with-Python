# Removing set items implies deleting elements from a set

# remove() Method
lang = {"C", "C++", "C#"}
lang.remove("C++")
print(lang)

# discard() Method
lang.discard("C#")
print(lang)

# pop() Method
# If the set is empty, the pop() method will raise a KeyError exception.
lang = {"C", "C++", "C#"}
lang.pop()
print(lang)
lang.pop()
print(lang)

# Note: 
# Sets in Python are unordered collections, so they don’t have a fixed order.
# That’s why .pop() just removes some element (implementation-dependent, but often the "first" in internal storage).

# clear() Method
lang.clear()
print(lang)

# Remove Items Existing in Both Sets
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print ("s1 after running difference_update: ", s1)

# Remove Items Existing in Either of the Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Removing items that exist in either set 
result_set = set1 ^ set2
print("Resulting Set:", result_set)

# Remove Uncommon Set Items
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Keeping only common items in set1
set1.intersection_update(set2)
print("Set 1 after keeping only common items:", set1)

# intersection() Method
# set.intersection(obj)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.intersection(s2)
print ("s3 = s1 & s2: ", s3)

# Symmetric Difference Update of Set Items
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s1.symmetric_difference_update(s2)
print ("s1 after running symmetric difference ", s1)

# Symmetric Difference of Set Items
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.symmetric_difference(s2)
print ("s1 = s1^s2 ", s3)