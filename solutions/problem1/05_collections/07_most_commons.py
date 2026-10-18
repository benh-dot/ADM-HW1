#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    # most frequent first, ties broken alphabetically
    top = sorted(Counter(s).items(), key=lambda kv: (-kv[1], kv[0]))[:3]
    for char, count in top:
        print(char, count)
