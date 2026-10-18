n, m = map(int, input().split())
arr = input().split()
A = set(input().split())
B = set(input().split())

# +1 for each element liked, -1 for each element disliked (O(1) set lookups)
print(sum((x in A) - (x in B) for x in arr))
