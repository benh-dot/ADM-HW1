n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(s, cmd)(*map(int, args))   # pop / remove x / discard x

print(sum(s))
