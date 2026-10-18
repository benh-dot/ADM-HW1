#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # same place after n >= 0 jumps:  x1 + n*v1 == x2 + n*v2
    #   =>  n = (x2 - x1) / (v1 - v2)  must be a non-negative integer
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    n, remainder = divmod(x2 - x1, v1 - v2)
    return "YES" if remainder == 0 and n >= 0 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
