# -----------------------------
# Basic Strings
# -----------------------------
text = "Hello, World!"
print("Original text:", text)

# Accessing characters
print("Second character:", text[1])
print("Last character:", text[-1])

# Slicing substrings
print("Characters 3 to 5:", text[2:5])
print("Third-last to second-last:", text[-5:-2])

# String length
print("Length of text:", len(text))

# -----------------------------
# Multi-line Strings
# -----------------------------
multi_line = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print("\nMulti-line string:")
print(multi_line)

# -----------------------------
# String Methods
# -----------------------------
print("\nString methods examples:")
print("Strip whitespace:", text.strip())  # removes leading/trailing spaces
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Replace H with J:", text.replace("H", "J"))
print("Split into words:", text.split(" "))

# -----------------------------
# Checking Substrings
# -----------------------------
sentence = "The rain in Spain stays mainly in the plain"
contains = "ain" in sentence
print("\nDoes the sentence contain 'ain'? :", contains)

# -----------------------------
# String Concatenation
# -----------------------------
greeting1 = "Hello "
greeting2 = "World"
full_greeting = greeting1 + greeting2
print("\nConcatenated string:", full_greeting)
