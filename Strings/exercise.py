# Python program to find number of vowels in a given string.

text    = "My name is Mohammed Iftekahr"
vowels  = "aeiou"
count   = 0

for x in text:
    if x.lower() in vowels:
        count += 1
print("Number of vowels:", count)


# Convert a string with binary digits to integer.

binary_str = '101011001010'

def fun(bstr):
    for x in bstr:
        if x not in '01':
            return "Error. String with non-binary characters"
    num = int(bstr, 2)
    return num

print("binary:{} integer: {}".format(binary_str, fun(binary_str)))


# Drop all digits from a string.

digits = [str(x) for x in range(10)]
str1 = 'He12llo, Py00th55on!'

char = []
for x in str1:
    if x not in digits:
        char.append(x)

str2 = "".join(char)
print(str2)  # Hello, Python!
