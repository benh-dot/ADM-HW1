import re

# only && / || with a space on both sides
pattern = re.compile(r'(?<= )(&&|\|\|)(?= )')
replace = lambda m: "and" if m.group(1) == "&&" else "or"

for _ in range(int(input())):
    print(pattern.sub(replace, input()))
