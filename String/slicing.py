# String slicing is a way of creating a sub-string from a given string.
# It allows you to extract a portion of the string by specifying a range of indices.

var = "HELLO PYTHON"
print(var[0])   # H
print(var[7])   # P
print(var[11])  # N
print(var[12])  # IndexError: string index out of range
print(var[-1])  # N 
print(var[-5])  # O 
print(var[-12]) # H

# Note: In Python, string is an immutable object. The object is immutable if it cannot be modified in-place, once stored in a certain memory location. You can retrieve any character from the string with the help of its index, but you cannot replace it with another character.

# SLicing with negative index
print ("var[3:8]:", var[3:8])
print ("var[-9:-4]:", var[-9:-4])