# Create a new dictionary by extracting the keys from a given dictionary.

dic1 = {
    "one": 1,
    "two": 2,
    "three": 3
}

print(dic1.keys())

arr1 = ["one", "three"]
dic2 = {}

for x in arr1:
    dic2[x] = dic1[x]
    
print(dic2)

# Convert a dictionary to list of (k,v) tuples.
dic1 = {
    "one": 1,
    "two": 2,
    "three": 3
}

list1 = list(dic1.items())
print(list1)

# Remove keys with same values in a dictionary.
dic1 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 3,
    "five": 1
}

values = list(dic1.values())
dic2 = {}
print(values)

unique = [x for x in values if values.count(x) == 1]

print(unique)

for y,z in dic1.items():
    if z in unique:
        d = {y:z}
        dic2.update(d)
        
print(dic2)