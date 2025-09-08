langs = {"C", "C++", "Java", "Python"}

# For Loop
for lang in langs:
    print(lang)
    
# List Comprehension
items = [item for item in langs]
print(items)

# Subset From a Set
import itertools

subsets = [set(subset) for subset in itertools.combinations(langs, 2)]
print(subsets)

# Checking if Set Item Exists
if "Java" in langs:
    print(True)
else:
    print(False)
