import numpy

numpy.set_printoptions(legacy='1.13')

def arrays(arr):
    # reversed, as floats
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
