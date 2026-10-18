A = set(input().split())
n = int(input())
# read all n sets (no early exit, so the whole input is consumed)
others = [set(input().split()) for _ in range(n)]
print(all(A > other for other in others))
