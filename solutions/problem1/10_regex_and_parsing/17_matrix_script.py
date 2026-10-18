#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# read column by column, top to bottom
decoded = "".join(matrix[r][c] for c in range(m) for r in range(n))
# non-alphanumeric runs *between* two alphanumerics become one space
print(re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded))
