n = int(input().strip())

# odd -> Weird; even in [6, 20] -> Weird; otherwise Not Weird
if n % 2 == 1 or 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
