from collections import defaultdict

n, m = map(int, input().split())
positions = defaultdict(list)
for i in range(1, n + 1):
    positions[input()].append(i)

for _ in range(m):
    word = input()
    print(" ".join(map(str, positions[word])) if word in positions else -1)
