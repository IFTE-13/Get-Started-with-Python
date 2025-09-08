# Adding items means inserting new key-value pairs into an existing dictionary.

# Square Brackets
student = {"name": "Alice", "age": 21}
print("Initial dictionary:", student)

student["major"] = "Computer Science"
print("After adding 'major':", student)

# the update() Method
student = {"name": "Alice", "age": 21}
print("\nInitial dictionary:", student)

student.update({"major": "Computer Science", "city": "New York"})
print("After update:", student)

# Dictionary Unpacking (** operator)
student = {"name": "Alice", "age": 21}
new_info = {"major": "Computer Science", "city": "New York"}
combined = {**student, **new_info}

print("\nBefore unpacking:", student)
print("After unpacking merge:", combined)

# the Union Operator (Python 3.9+)
student = {"name": "Alice", "age": 21}
new_info = {"major": "Computer Science", "city": "New York"}
merged = student | new_info

print("\nBefore union:", student)
print("After union merge:", merged)

# the |= Operator (Python 3.9+)
student = {"name": "Alice", "age": 21}
new_info = {"major": "Computer Science", "city": "New York"}
student |= new_info

print("\nAfter |= merge:", student)

# setdefault() Method
student = {"name": "Alice", "age": 21}
student.setdefault("major", "Computer Science")
print("\nAfter setdefault():", student)

# collections.defaultdict()
from collections import defaultdict

# Using int as the default factory (missing keys → 0)
student_scores = defaultdict(int)
student_scores["math"] += 1
print("\nUsing defaultdict(int):", dict(student_scores))

# Using list as the default factory (missing keys → empty list)
student_courses = defaultdict(list)
student_courses["courses"].append("Math")
print("Using defaultdict(list):", dict(student_courses))

# Using a custom function as default factory
def default_value():
    return "N/A"

student_profile = defaultdict(default_value)
print("Accessing missing key:", student_profile["hobby"])
