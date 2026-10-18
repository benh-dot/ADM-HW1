import re

css = "\n".join(input() for _ in range(int(input())))

# colours only appear inside { ... } blocks (selectors like #BED are outside)
hex_color = re.compile(r'#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?![0-9a-zA-Z])')
for block in re.findall(r'\{([^}]*)\}', css):
    for color in hex_color.findall(block):
        print(color)
