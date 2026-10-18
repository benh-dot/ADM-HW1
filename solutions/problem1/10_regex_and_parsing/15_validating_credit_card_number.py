import re

# starts with 4/5/6, 16 digits, optionally in groups of 4 separated by "-"
fmt = re.compile(r'^[456]\d{3}(-?\d{4}){3}$')
# 4 or more consecutive repeated digits
repeated = re.compile(r'(\d)\1{3}')

for _ in range(int(input())):
    card = input().strip()
    ok = fmt.match(card) and not repeated.search(card.replace("-", ""))
    print("Valid" if ok else "Invalid")
