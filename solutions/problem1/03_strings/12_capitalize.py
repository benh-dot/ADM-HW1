#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    # split on single spaces so that multiple spaces are preserved, and only
    # upper-case the first character (str.title() would break "12abc")
    return " ".join(word[:1].upper() + word[1:] for word in s.split(" "))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
