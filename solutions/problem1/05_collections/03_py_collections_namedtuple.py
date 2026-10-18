from collections import namedtuple

n = int(input())
Student = namedtuple("Student", input().split())   # columns can be in any order
students = [Student(*input().split()) for _ in range(n)]
print(f"{sum(int(s.MARKS) for s in students) / n:.2f}")
