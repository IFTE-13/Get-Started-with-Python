# Same Dictionary Example (student_info)
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Square Brackets []
print("Name:", student_info["name"])

# get() Method
print("Age:", student_info.get("age"))

# Dictionary Keys
keys = student_info.keys()
print("Keys:", keys)

# Accessing values individually
name = student_info["name"]
age = student_info.get("age")
major = student_info["major"]
print("Name:", name)
print("Age:", age)
print("Major:", major)

# Dictionary Values
print("Values:", student_info.values())

# items() Function
all_items = student_info.items()
print("Items:", all_items)

# Iterating through the key-value pairs
print("Iterating through key-value pairs:")
for key, value in all_items:
    print(f"{key}: {value}")
