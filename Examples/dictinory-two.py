# Vowels dictionary
vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
print("\nVowels dictionary:", vowels)

# Using dict() constructor
vowels2 = dict([(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')])
print("Vowels dictionary (using dict constructor):", vowels2)

# Access specific value
print("Vowel at key 1:", vowels[1])

# List all keys
print("All keys:", vowels.keys())

# List all values
print("All values:", vowels.values())