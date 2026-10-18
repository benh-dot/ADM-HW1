def is_valid(uid):
    return (len(uid) == 10
            and uid.isalnum()
            and len(set(uid)) == 10                       # no repeated characters
            and sum(c.isupper() for c in uid) >= 2
            and sum(c.isdigit() for c in uid) >= 3)


for _ in range(int(input())):
    print("Valid" if is_valid(input().strip()) else "Invalid")
