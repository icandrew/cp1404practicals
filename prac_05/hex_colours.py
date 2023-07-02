"""
CP1404/CP5632 Practical
Color Hex
"""

COLOR_TO_HEX = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                "Antique White": "#faebd7", "Antique White 1": "#ffefdb", "Antique White 2": "#eedfcc"}

color_name = input("Color Name:").lower()
while color_name != "":
    colors = (color.lower() for color in COLOR_TO_HEX.keys())
    if color_name in colors:
        print(f"{color_name} is available")
        color_name = input("Enter Color: ").lower()
    else:
        print("Invalid Color")
        color_name = input("Enter Color: ").lower()
