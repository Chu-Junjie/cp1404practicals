# Constant dictionary of colour names and hex codes
COLOUR_HEX_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

# Input loop for user to enter colour names
colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_HEX_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
