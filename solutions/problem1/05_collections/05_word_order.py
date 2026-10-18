from collections import Counter

words = [input().strip() for _ in range(int(input()))]
counts = Counter(words)          # keeps first-insertion order (Python 3.7+)
print(len(counts))
print(*counts.values())
