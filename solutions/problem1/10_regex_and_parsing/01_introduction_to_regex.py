import re

# optional sign, any digits, a mandatory dot, at least one digit after it
pattern = re.compile(r'^[+-]?\d*\.\d+$')
for _ in range(int(input())):
    print(bool(pattern.match(input().strip())))
