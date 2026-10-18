n, m = map(int, input().split())

# top half: 1, 3, 5, ... patterns, centred with dashes
for i in range(n // 2):
    print((".|." * (2 * i + 1)).center(m, "-"))
print("WELCOME".center(m, "-"))
# bottom half mirrors the top
for i in reversed(range(n // 2)):
    print((".|." * (2 * i + 1)).center(m, "-"))
