n, x = map(int, input().split())
subjects = [map(float, input().split()) for _ in range(x)]

# zip(*subjects) groups the marks of the same student together
for marks in zip(*subjects):
    print(f"{sum(marks) / x:.1f}")
