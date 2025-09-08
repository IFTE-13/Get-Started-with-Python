# 1. Find the largest number in an array
import array as arr

a = arr.array('i', [10, 5, 15, 4, 6, 20, 9])
largest = a[0]
for i in range(1, len(a)):
    if a[i] > largest:
        largest = a[i]

print("Largest number:", largest)
# Output: Largest number: 20

# 2. Store all even numbers from an array in another array
even_numbers = arr.array('i')
for i in range(len(a)):
    if a[i] % 2 == 0:
        even_numbers.append(a[i])

print("Even numbers (sorted):", sorted(even_numbers))
# Output: Even numbers (sorted): [4, 6, 10, 20]

# 3. Average of all numbers in an array
total = 0
for i in range(len(a)):
    total += a[i]

average = total / len(a)
print("Average (manual calculation):", average)
# Output: Average (manual calculation): 9.857142857142858

# Or using sum() function
print("Average (using sum()):", sum(a) / len(a))
# Output: Average (using sum()): 9.857142857142858
