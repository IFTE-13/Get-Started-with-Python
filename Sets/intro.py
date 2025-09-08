# A set is an unordered collection of unique elements. Unlike lists or tuples, sets do not allow duplicate values i.e. each element in a set must be unique. Sets are mutable, meaning you can add or remove items after a set has been created.

# converting list into set using set() Method
my_set = set([1, 2, 3, 4, 5])
print (my_set)

# Duplicate Elements
my_set = {1, 2, 3, 2, 3, 4, 5, 5}
print(my_set)

# Mixed Set
mixed_set = {1, 'hello', (1, 2, 3)}
print (mixed_set)

# Frozen Set
frozen_set = frozenset([1, 2, 3])
print(frozen_set)
frozen_set.add(4)