# Set is mutable. Which means we can modify them after they have been created.

# add() Method
# set.add(obj)
lang = set()
lang.add("C")
lang.add("C++")
lang.add("C-")
lang.add("C#")
print(lang)

# update() Method
# set.update(obj)
lang.update(["Java", "Python"])
print(lang)

# Ex:2
up = {"PHP", "JS"}
lang.update(up)
print(lang)

# Union Operator
up2 = {"R", "Ruby"}
new_lang = lang | up2
print(new_lang)

# Set Comprehension
numbers = [1, 2, 3, 4, 5]

square_set = {num ** 2 for num in numbers}
print(square_set)