# Find unique numbers in a given list.
L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []

for x in L1:
    if x not in L2:
        L2.append(x)
L2.sort()
print(L2) 

# Find sum of all numbers
L1 = [1, 9, 1, 6, 3, 4]
ttl = 0

for x in L1:
    ttl += x

print(ttl)

# List of 5 random integers.
import random

L1 = []
for i in range(5):
    x = random.randint(0, 100)
    L1.append(x)
    
print(L1)