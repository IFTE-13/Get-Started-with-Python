# Unicode is universal character encodign standard
# Python 3.x uses Unicode by default for strings.
# Every str object is a sequence of Unicode characters.

text = "Hello, Iftekhar"
print(type(text))  # <class 'str'>

# encoding -> str  to bytes
text = "Hello, Iftekhar"
encoded = text.encode("utf-8")
print(encoded)
print(type(encoded))  # <class 'bytes'>

# decoding -> bytes to str
decoded = encoded.decode("utf-8")
print(decoded)

# Common encodings:
# "utf-8" → most popular, variable-length, supports all Unicode.
# "ascii" → only 128 chars, will fail for non-English.
# "utf-16", "utf-32" → fixed-width, less common.

# Unicode code points:
# Each character has a unique code point, e.g., 'A' is U+004
# You can get code point using ord() and chr()
char = 'A'  
print(ord(char))     # 65
print(chr(65))       # 'A'
print(chr(0x1F600))  # 😀

# Unicode in Strings
# string length
s = "Hello, 😀"
print(len(s))  # 8 (counting characters, not bytes)

# Iterating over characters
for c in s:
    print(c)
    