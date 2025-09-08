# A book has a cover price of $24.95, but bookstores receive a 40% discount. Shipping costs $3 for the first copy and $0.75 for each additional copy.

# Task: Calculate the total wholesale cost for 60 copies of the book, including shipping.

# Book details
cover_price = 24.95
discount_rate = 0.40  # 40% discount
num_copies = 60

# Calculate discounted price per book
discount_amount = cover_price * discount_rate
wholesale_price = cover_price - discount_amount

# Total cost for books
total_books_cost = wholesale_price * num_copies

# Shipping cost: $3 for first copy + $0.75 for each additional copy
shipping_cost = 3 + 0.75 * (num_copies - 1)

# Total wholesale cost including shipping
total_wholesale_cost = total_books_cost + shipping_cost

# Print result
print(f"Total wholesale cost for {num_copies} copies: ${total_wholesale_cost:.2f}")
