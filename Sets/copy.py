# copy() Method
# set.copy()

lang = {"C", "C++", "Java", "Python"}

lang1 = lang.copy()
lang.add("PHP")

print(lang)
print(lang1)

# set() Function
original_set = {1, 2, 3, 4}

copy_set = set(original_set)

copy_set.add(5)

print(original_set)
print(copy_set)

# Set Comprehension
# {expression for item in iterable if condition}

original_set = {1, 2, 3, 4, 5}
copied_set  = {x for x in original_set}

print(copied_set)