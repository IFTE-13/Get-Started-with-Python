# "|" Operator
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1|s2
print (s3)

# union() Method
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.union(s2)
print (s3)

# Unpacking Operator
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = {*s1, *s2}
print (s3)

# Set Comprehension
set1 = {1, 2, 3}
set2 = {3, 4, 5}

joined_set = {x for s in [set1, set2] for x in s}
print(joined_set)

# Iterative Addition
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Initializing an empty set to hold the merged elements
joined_set = set()

# Iterating over set1 and adding its elements to the joined set
for element in set1:
   joined_set.add(element)
   
# Iterating over set2 and adding its elements to the joined set
for element in set2:
   joined_set.add(element)

print(joined_set)  