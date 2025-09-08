# Function to draw a grid
def grids(area, unit):
    for _ in range(area):
        print(("+" + "- " * unit) * area + "+")
        for _ in range(unit):
            print(("|" + "  " * unit) * area + "|")
    print(("+" + "- " * unit) * area + "+")


grids(2, 5)