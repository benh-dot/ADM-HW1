import re

S = input()
k = input()

# a zero-width lookahead finds overlapping matches too
found = False
for m in re.finditer(r'(?=' + re.escape(k) + r')', S):
    found = True
    print((m.start(), m.start() + len(k) - 1))
if not found:
    print((-1, -1))
