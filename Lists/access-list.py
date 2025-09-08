# Indexing
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]

print ("Item at 0th index in list1: ", list1[0])
print ("Item at index 2 in list2: ", list2[2])

# Negative Indexing
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Item at 0th index in list1: ", list1[-1])
print ("Item at index 2 in list2: ", list2[-3])

# Slice Operator
# [start:stop] 
# start is the starting index (inclusive).
# stop is the ending index (exclusive).
# [ : ] starts from 0 index and ends at n-th index
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]
list3 = ["Rohan", "Physics", 21, 69.75]

print ("Items from index 1 to last in list1: ", list1[1:])
print ("Items from index 0 to 1 in list2: ", list2[:2])
print ("Items from index 0 to index last in list3", list3[:])

# Sub List
# part of a list that consists of a consecutive sequence of elements from the original list
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Items from index 1 to 2 in list1: ", list1[1:3])
print ("Items from index 0 to 1 in list2: ", list2[0:2])