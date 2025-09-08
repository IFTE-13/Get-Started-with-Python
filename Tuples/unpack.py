# The term "unpacking" refers to the process of parsing tuple items in individual variables. 

t1 = (10, 20, 30)
x, y, z = t1
print(x, y, z)

# ValueError While Unpacking a Tuple
# If the number of variables is more or less than the length of tuple, Python raises a ValueError.

# Using Asterisk (*)
tup1 = (10,20,30)
x, *y = tup1
print ("x:", x, " ", "y:", y) # x:  10 y:  [20, 30]

