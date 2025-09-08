# Removing dictionary items in Python refers to deleting key-value pairs from an existing dictionary.

# Initial dictionary
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
print("Initial dictionary:", student)

# del keyword
del student["age"]
print("\nAfter del operation:", student)

# pop() method
removed_value = student.pop("major")
print("\nAfter pop operation:", student)
print("Value popped:", removed_value)

# popitem() method
removed_item = student.popitem()
print("\nAfter popitem operation:", student)
print("Item popped:", removed_item)

# Rebuilding the dictionary for further operations
student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# clear() method
student.clear()
print("\nAfter clear method:", student)

# Rebuilding again for conditional removal
student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# pop() in a loop
keys_to_remove = ["age", "major"]
for key in keys_to_remove:
    student.pop(key, None)
print("\nAfter conditional removal:", student)

# 6. Conditional removal using dictionary comprehension (remove all int values)
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
student = {k: v for k, v in student.items() if not isinstance(v, int)}
print("\nAfter dictionary comprehension removal:", student)
