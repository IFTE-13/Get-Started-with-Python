# common elements in two lists with the help of set operations
l1 = [1, 2, 3, 4]
l2 = [4, 5, 6, 2]

s1 = set(l1)
s2 = set(l2)

commons = s1 & s2
print(list(commons))

# Check if a set is a subset of another
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}

if s2.issubset(s1):
    print(True)
else:
    print(False)
    
# List of unique elements in a list
T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)

s1 = set(T1)

print(s1)