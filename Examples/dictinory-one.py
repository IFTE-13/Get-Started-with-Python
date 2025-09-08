# Car information using a dictionary
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2018,
    "price": 20000
}

# Print the whole dictionary
print("Car information:", car)

# Access a specific value using key
print("Car model:", car["model"])

# Update a value
car["year"] = 2022
print("Updated car info:", car)

# Loop through keys
print("\nKeys in car dictionary:")
for key in car:
    print(key)

# Loop through values
print("\nValues in car dictionary:")
for value in car.values():
    print(value)

# Loop through both keys and values
print("\nCar details (key: value):")
for key, value in car.items():
    print(f"{key}: {value}")

# Check if a key exists
if "model" in car:
    print('\nYes, "model" is one of the keys in the car dictionary')

# Length of the dictionary
print("\nNumber of attributes in car dictionary:", len(car))

# Add a new key-value pair
car["color"] = "blue"
print("After adding color:", car)

# Remove a specific key-value pair
car.pop("price")
print("After removing price:", car)

# Remove the last inserted key-value pair
car.popitem()
print("After removing the last item:", car)