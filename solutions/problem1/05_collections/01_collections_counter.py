from collections import Counter

input()
stock = Counter(map(int, input().split()))
earned = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if stock[size] > 0:
        stock[size] -= 1
        earned += price
print(earned)
