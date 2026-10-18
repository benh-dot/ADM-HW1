s = input()

# order: lowercase < uppercase < odd digits < even digits, then by character
def rank(c):
    if c.islower():
        return (0, c)
    if c.isupper():
        return (1, c)
    if int(c) % 2 == 1:
        return (2, c)
    return (3, c)

print("".join(sorted(s, key=rank)))
