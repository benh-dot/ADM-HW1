import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
print(round(numpy.linalg.det(a), 2))
