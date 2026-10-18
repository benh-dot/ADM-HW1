import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
# HackerRank expects the standard deviation rounded to 11 decimals
print(round(numpy.std(a), 11))
