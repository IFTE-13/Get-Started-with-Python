# The items(), keys(), and values() methods of a dictionary return view objects.
# These views are dynamic: if the dictionary is updated, the view reflects the changes automatically.

# Initial dictionary
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
print("Initial dictionary:", student)

# 1. keys() Method
keys_view = student.keys()
print("\nType of keys_view:", type(keys_view))
print("Keys:", keys_view)

# Updating the dictionary
student.update({"city": "New York"})
print("After update, keys view automatically reflects changes:", keys_view)

# 2. values() Method
values_view = student.values()
print("\nType of values_view:", type(values_view))
print("Values:", values_view)

# Updating the dictionary
student.update({"hobby": "Reading"})
print("After update, values view automatically reflects changes:", values_view)

# 3. items() Method
items_view = student.items()
print("\nType of items_view:", type(items_view))
print("Items:", items_view)

# Updating the dictionary
student.update({"graduated": False})
print("After update, items view automatically reflects changes:", items_view)
