# In Python, tuple is a sequence data type. It is an ordered collection of items. Each item in the tuple has a unique position index, starting from 0.

# In C/C++/Java array, the array elements must be of same type. On the other hand, Python tuple may have objects of different data types.

# Python tuple and list both are sequences. One major difference between the two is, Python list is mutable, whereas tuple is immutable. Although any item from the tuple can be accessed using its index, and cannot be modified, removed or added.


# Accessing with Indexing
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

# Accessing with Negative Indexing
tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)
print ("Item at 0th index in tup1: ", tup1[-1])
print ("Items from index 2 to last in tup2", tup2[2:-1])

# Accessing with Slice Operator
# [start:stop]
tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)
tuple3 = (1, 2, 3, 4, 5)
tuple4 = ("Rohan", "Physics", 21, 69.75)
print ("Items from index 1 to last in tuple1: ", tuple1[1:])
print ("Items from index 0 to 1 in tuple2: ", tuple2[:2])
print ("Items from index 0 to index last in tuple3", tuple3[:])

# Accessing Sub Tuple from Tuple
# my_tuple[start:stop]
# start is the starting index (inclusive).
# stop is the ending index (exclusive) of the subtuple.
tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)
print ("Items from index 1 to 2 in tuple1: ", tuple1[1:3])
print ("Items from index 0 to 1 in tuple2: ", tuple2[0:2])