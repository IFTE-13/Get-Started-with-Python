# -----------------------------
# Example: Fruits List
# -----------------------------
fruits = ["apple", "banana", "pineapple", "kiwi", "melon", "mango"]
print("Original list:", fruits)

# Accessing elements
print("Second item:", fruits[1])
print("Last item:", fruits[-1])

# Slicing
print("Items 3 to 5:", fruits[2:5])
print("First 4 items:", fruits[:4])
print("From third item to end:", fruits[2:])
print("From 3rd last to 2nd last:", fruits[-4:-1])

# Modifying elements
fruits[1] = "blackcurrant"
print("After modification:", fruits)

# Looping through a list
print("\nLooping through fruits:")
for fruit in fruits:
    print(fruit)

# Check if an item exists
if "apple" in fruits:
    print("\nYes, 'apple' is in the fruits list")

# List length
print("Number of fruits:", len(fruits))

# Adding elements
fruits.append("orange")  # add at the end
fruits.insert(1, "persimmon")  # add at specific index
print("After adding fruits:", fruits)

# Removing elements
fruits.pop()  # removes last element
del fruits[0]  # deletes element at index 0
fruits.remove("kiwi")  # removes specific element
print("After removing fruits:", fruits)

# Copying lists
fruits_copy = fruits.copy()  # independent copy
fruits_ref = fruits  # reference, changes affect original
print("Copied list:", fruits_copy)
print("Reference list:", fruits_ref)

# Combining lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
combined_list = list1 + list2
print("Combined list:", combined_list)

# Reversing and extending
fruits.reverse()  # reverse in place
print("Reversed list:", fruits)

fruits.extend(["grape", "papaya"])  # concatenate another list
print("Extended list:", fruits)

# -----------------------------
# List Comprehensions
# -----------------------------
numbers = [0, 5, 10]
doubled = [x*2 for x in numbers]  # multiply each element by 2
print("Original numbers:", numbers)
print("Doubled numbers:", doubled)

# -----------------------------
# Accessing elements safely
# -----------------------------
mixed_list = [1, 2, 3, "apple", "banana", "orange"]
print("\nMixed list:", mixed_list)
print("First element:", mixed_list[0])

# Slicing examples
print("Items 3 to 5:", mixed_list[2:5])
print("First 4 items:", mixed_list[:4])
print("From third item to end:", mixed_list[2:])
print("From 4th last to 2nd last:", mixed_list[-4:-1])
