k = int(input())
rooms = list(map(int, input().split()))

# every family room appears k times, the captain's room once:
#   k * sum(distinct) - sum(all) = (k - 1) * captain
print((k * sum(set(rooms)) - sum(rooms)) // (k - 1))
