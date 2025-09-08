# Information
# -> Built-in data type
# -> Multiple data type acceptable
# -> Index starts from 0 (zero)
# -> List in Python is similar to an array in C, C++ or Java. However, the major difference is that in C/C++/Java, the array elements must be of same type. On the other hand, Python lists may have objects of different data types.

# Example
# Accessing Values
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])      # list1[0]:  physics
print ("list2[1:5]: ", list2[1:5])  # list2[1:5]:  [2, 3, 4, 5]

# Updating
list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001
print ("New value available at index 2 : ")
print (list[2])

# Delete Elements
list1 = ['physics', 'chemistry', 1997, 2000]
print (list1)
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)