input()
A = set(map(int, input().split()))

for _ in range(int(input())):
    operation, _size = input().split()
    other = set(map(int, input().split()))
    getattr(A, operation)(other)   # update / intersection_update / ...

print(sum(A))
