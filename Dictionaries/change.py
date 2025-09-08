# Changing dictionary items means modifying, adding, or removing key-value pairs.
# Dictionaries are mutable, so updates are always possible.

# Initial dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Initial:", person)

# Modifying the value of an existing key
person["age"] = 26
print("After modifying 'age':", person)

# Updating multiple values using update()
person.update({"age": 27, "city": "Los Angeles"})
print("After updating multiple values:", person)

# Conditional modification
if person["age"] == 27:
    person["age"] = 28
print("After conditional modification:", person)

# Adding a new key-value pair
person["profession"] = "Engineer"
print("After adding 'profession':", person)

# Using setdefault() (adds key only if it doesn’t exist)
person.setdefault("hobby", "Reading")
print("After setdefault (hobby):", person)

# Removing a key-value pair using del
del person["city"]
print("After deleting 'city':", person)

# Removing and returning a value using pop()
removed_age = person.pop("age")
print("After popping 'age':", person)
print("Removed age:", removed_age)

# Removing the last inserted item using popitem()
removed_item = person.popitem()
print("After popitem:", person)
print("Removed item:", removed_item)
