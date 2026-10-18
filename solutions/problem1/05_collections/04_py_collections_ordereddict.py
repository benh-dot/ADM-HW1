from collections import OrderedDict

totals = OrderedDict()
for _ in range(int(input())):
    *name, price = input().split()
    item = " ".join(name)
    totals[item] = totals.get(item, 0) + int(price)

for item, total in totals.items():
    print(item, total)
