from collections import deque

for _ in range(int(input())):
    input()
    cubes = deque(map(int, input().split()))
    top = float("inf")
    ok = True
    while cubes:
        # greedily take the larger of the two ends
        cube = cubes.popleft() if cubes[0] >= cubes[-1] else cubes.pop()
        if cube > top:
            ok = False
            break
        top = cube
    print("Yes" if ok else "No")
