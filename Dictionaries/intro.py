# A dictionary is a built-in data type that stores data in key-value pairs.
# Unordered: The items do not follow insertion order (Python 3.7+ preserves insertion order, but logically it's unordered).
# Mutable: You can add, update, or remove key-value pairs.
# Indexed: Values are accessed using keys, not numeric indices.
# Unique Keys: Each key must be unique within the dictionary.
# Heterogeneous: Keys and values can be of any data type.

# Example:
numbers = {
    10: "Ten",
    20: "Twenty",
    30: "Thirty",
    40: "Forty"
}

# Accessing values
print("Value for key 10:", numbers[10])     # Using square brackets
print("Value for key 20:", numbers.get(20)) # Using get() method

# Displaying dictionary features
print("Keys:", numbers.keys())
print("Values:", numbers.values())
print("Items (key-value pairs):", numbers.items())

# Iterating through dictionary
print("\nIterating through dictionary:")
for key, value in numbers.items():
    print(f"{key} ➝ {value}")
