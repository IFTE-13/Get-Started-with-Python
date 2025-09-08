# -----------------------------
# Example 1: Print words with more than 20 characters
# -----------------------------
# Open the file in read mode
with open('file.txt', 'r') as data:
    print("Words with more than 20 characters:")
    for line in data:
        for word in line.split():
            if len(word) > 20:  # check word length
                print(word)

# -----------------------------
# Example 2: Print words that do NOT contain the letter 'e'
# -----------------------------
def words_without_letter(filename, letter):
    with open(filename, 'r') as file:
        print(f"\nWords without the letter '{letter}':")
        for line in file:
            for word in line.split():
                if letter.lower() not in word.lower():  # case-insensitive check
                    print(word)

words_without_letter('file.txt', 'e')

# -----------------------------
# Example 3: Cumulative sum of a list of numbers
# -----------------------------
def cumulative_sum(numbers):
    """
    Returns a new list where each element is the cumulative sum
    of elements from the original list.
    """
    total = 0
    result = []
    for num in numbers:
        total += num
        result.append(total)
    return result

# Example usage
nums = [1, 2, 3, 4, 5]
print("\nOriginal list:", nums)
print("Cumulative sum:", cumulative_sum(nums))
