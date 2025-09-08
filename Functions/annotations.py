# Function annotation feature of Python enables you to add additional explanatory metadata about the arguments declared in a function definition

def add(a: int, b: int) -> int:
    return a + b
print("Sum:", add(5, 3))       # 8
print("Sum:", add(5.5, 3.2), add.__annotations__)   # 8.7
print (add("Hello ", "Python"), add.__annotations__) # Hello Python {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

# Python does not enforce type hints at runtime.
# They are just metadata (stored in __annotations__) and mainly used by:
# tools like mypy (static type checker),
# IDEs for autocomplete / linting,
# documentation.
# So even though it's hinted that a and b should be int, Python will happily # allow float or even str — because the + operator works on them.

# Annotations = hints, not rules
