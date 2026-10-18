"""
Algorithmic Methods of Data Mining - Homework 1
================================================

All HackerRank solutions for Problem 1 (Python domain) and Problem 2
(algorithms), one function per challenge, grouped by section.

The body of each function is exactly the code submitted on HackerRank
(the same code is also available as one file per challenge in solutions/).

Usage
-----
    python scripts.py list                 # list every solution
    python scripts.py <name> < input.txt   # run one solution on an input

Challenges whose HackerRank template writes to OUTPUT_PATH are handled
automatically: if OUTPUT_PATH is not set, the result is printed instead.
"""
import os
import sys
import tempfile


###########################################################################
#                      PROBLEM 1 - Python challenges                      #
###########################################################################

# =========================================================================
# Introduction (7 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Say "Hello, World!" With Python
# https://www.hackerrank.com/challenges/py-hello-world/problem
# -------------------------------------------------------------------------
def p1_01_01_py_hello_world():
    print("Hello, World!")


# -------------------------------------------------------------------------
# Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem
# -------------------------------------------------------------------------
def p1_01_02_py_if_else():
    n = int(input().strip())

    # odd -> Weird; even in [6, 20] -> Weird; otherwise Not Weird
    if n % 2 == 1 or 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# -------------------------------------------------------------------------
# Arithmetic Operators
# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# -------------------------------------------------------------------------
def p1_01_03_python_arithmetic_operators():
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        print(a + b)
        print(a - b)
        print(a * b)


# -------------------------------------------------------------------------
# Python: Division
# https://www.hackerrank.com/challenges/python-division/problem
# -------------------------------------------------------------------------
def p1_01_04_python_division():
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        print(a // b)
        print(a / b)


# -------------------------------------------------------------------------
# Loops
# https://www.hackerrank.com/challenges/python-loops/problem
# -------------------------------------------------------------------------
def p1_01_05_python_loops():
    if __name__ == '__main__':
        n = int(input())
        for i in range(n):
            print(i ** 2)


# -------------------------------------------------------------------------
# Write a function
# https://www.hackerrank.com/challenges/write-a-function/problem
# -------------------------------------------------------------------------
def p1_01_06_write_a_function():
    def is_leap(year):
        # divisible by 4, except centuries unless divisible by 400
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


    year = int(input())
    print(is_leap(year))


# -------------------------------------------------------------------------
# Print Function
# https://www.hackerrank.com/challenges/python-print/problem
# -------------------------------------------------------------------------
def p1_01_07_python_print():
    if __name__ == '__main__':
        n = int(input())
        print(*range(1, n + 1), sep="")

# =========================================================================
# Basic Data Types (6 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# List Comprehensions
# https://www.hackerrank.com/challenges/list-comprehensions/problem
# -------------------------------------------------------------------------
def p1_02_01_list_comprehensions():
    if __name__ == '__main__':
        x = int(input())
        y = int(input())
        z = int(input())
        n = int(input())
        print([[i, j, k]
               for i in range(x + 1)
               for j in range(y + 1)
               for k in range(z + 1)
               if i + j + k != n])


# -------------------------------------------------------------------------
# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# -------------------------------------------------------------------------
def p1_02_02_find_second_maximum_number_in_a_list():
    if __name__ == '__main__':
        n = int(input())
        arr = map(int, input().split())
        # distinct scores, sorted: the runner-up is the second largest
        print(sorted(set(arr))[-2])


# -------------------------------------------------------------------------
# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem
# -------------------------------------------------------------------------
def p1_02_03_nested_list():
    if __name__ == '__main__':
        records = []
        for _ in range(int(input())):
            name = input()
            score = float(input())
            records.append([name, score])

        second_lowest = sorted(set(score for _, score in records))[1]
        for name in sorted(name for name, score in records if score == second_lowest):
            print(name)


# -------------------------------------------------------------------------
# Finding the percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# -------------------------------------------------------------------------
def p1_02_04_finding_the_percentage():
    if __name__ == '__main__':
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()

        marks = student_marks[query_name]
        print(f"{sum(marks) / len(marks):.2f}")


# -------------------------------------------------------------------------
# Lists
# https://www.hackerrank.com/challenges/python-lists/problem
# -------------------------------------------------------------------------
def p1_02_05_python_lists():
    if __name__ == '__main__':
        N = int(input())
        lst = []
        for _ in range(N):
            cmd, *args = input().split()
            args = list(map(int, args))
            if cmd == "print":
                print(lst)
            else:
                # insert, remove, append, sort, pop, reverse are list methods
                getattr(lst, cmd)(*args)


# -------------------------------------------------------------------------
# Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem
# -------------------------------------------------------------------------
def p1_02_06_python_tuples():
    if __name__ == '__main__':
        n = int(input())
        integer_list = map(int, input().split())
        print(hash(tuple(integer_list)))

# =========================================================================
# Strings (14 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# sWAP cASE
# https://www.hackerrank.com/challenges/swap-case/problem
# -------------------------------------------------------------------------
def p1_03_01_swap_case():
    def swap_case(s):
        return s.swapcase()


    if __name__ == '__main__':
        s = input()
        result = swap_case(s)
        print(result)


# -------------------------------------------------------------------------
# String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# -------------------------------------------------------------------------
def p1_03_02_python_string_split_and_join():
    def split_and_join(line):
        return "-".join(line.split(" "))


    if __name__ == '__main__':
        line = input()
        result = split_and_join(line)
        print(result)


# -------------------------------------------------------------------------
# What's Your Name?
# https://www.hackerrank.com/challenges/whats-your-name/problem
# -------------------------------------------------------------------------
def p1_03_03_whats_your_name():
    def print_full_name(first, last):
        print(f"Hello {first} {last}! You just delved into python.")


    if __name__ == '__main__':
        first_name = input()
        last_name = input()
        print_full_name(first_name, last_name)


# -------------------------------------------------------------------------
# Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem
# -------------------------------------------------------------------------
def p1_03_04_python_mutations():
    def mutate_string(string, position, character):
        # strings are immutable: rebuild it around the changed position
        return string[:position] + character + string[position + 1:]


    if __name__ == '__main__':
        s = input()
        i, c = input().split()
        s_new = mutate_string(s, int(i), c)
        print(s_new)


# -------------------------------------------------------------------------
# Find a string
# https://www.hackerrank.com/challenges/find-a-string/problem
# -------------------------------------------------------------------------
def p1_03_05_find_a_string():
    def count_substring(string, sub_string):
        # count overlapping occurrences
        return sum(1 for i in range(len(string) - len(sub_string) + 1)
                   if string[i:i + len(sub_string)] == sub_string)


    if __name__ == '__main__':
        string = input().strip()
        sub_string = input().strip()

        count = count_substring(string, sub_string)
        print(count)


# -------------------------------------------------------------------------
# String Validators
# https://www.hackerrank.com/challenges/string-validators/problem
# -------------------------------------------------------------------------
def p1_03_06_string_validators():
    if __name__ == '__main__':
        s = input()
        for check in (str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper):
            print(any(check(c) for c in s))


# -------------------------------------------------------------------------
# Text Alignment
# https://www.hackerrank.com/challenges/text-alignment/problem
# -------------------------------------------------------------------------
def p1_03_07_text_alignment():
    # Replace all ______ with rjust, ljust or center.

    thickness = int(input())  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


# -------------------------------------------------------------------------
# Text Wrap
# https://www.hackerrank.com/challenges/text-wrap/problem
# -------------------------------------------------------------------------
def p1_03_08_text_wrap():
    import textwrap


    def wrap(string, max_width):
        return textwrap.fill(string, max_width)


    if __name__ == '__main__':
        string, max_width = input(), int(input())
        result = wrap(string, max_width)
        print(result)


# -------------------------------------------------------------------------
# Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem
# -------------------------------------------------------------------------
def p1_03_09_designer_door_mat():
    n, m = map(int, input().split())

    # top half: 1, 3, 5, ... patterns, centred with dashes
    for i in range(n // 2):
        print((".|." * (2 * i + 1)).center(m, "-"))
    print("WELCOME".center(m, "-"))
    # bottom half mirrors the top
    for i in reversed(range(n // 2)):
        print((".|." * (2 * i + 1)).center(m, "-"))


# -------------------------------------------------------------------------
# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem
# -------------------------------------------------------------------------
def p1_03_10_python_string_formatting():
    def print_formatted(number):
        width = len(bin(number)) - 2  # width of the binary value of n
        for i in range(1, number + 1):
            print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")


    if __name__ == '__main__':
        n = int(input())
        print_formatted(n)


# -------------------------------------------------------------------------
# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# -------------------------------------------------------------------------
def p1_03_11_alphabet_rangoli():
    import string


    def print_rangoli(size):
        letters = string.ascii_lowercase[:size]
        width = 4 * size - 3
        rows = []
        for i in range(size):
            right = "-".join(letters[i:])          # e.g. "c-d-e"
            rows.append((right[::-1] + right[1:]).center(width, "-"))
        # rows[0] is the widest (middle) row; mirror it vertically
        print("\n".join(rows[::-1] + rows[1:]))


    if __name__ == '__main__':
        n = int(input())
        print_rangoli(n)


# -------------------------------------------------------------------------
# Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem
# -------------------------------------------------------------------------
def p1_03_12_capitalize():
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


# -------------------------------------------------------------------------
# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem
# -------------------------------------------------------------------------
def p1_03_13_the_minion_game():
    def minion_game(string):
        # every substring starting at position i: there are len(string) - i of them
        n = len(string)
        kevin = sum(n - i for i, ch in enumerate(string) if ch in "AEIOU")
        stuart = n * (n + 1) // 2 - kevin

        if stuart > kevin:
            print("Stuart", stuart)
        elif kevin > stuart:
            print("Kevin", kevin)
        else:
            print("Draw")


    if __name__ == '__main__':
        s = input()
        minion_game(s)


# -------------------------------------------------------------------------
# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem
# -------------------------------------------------------------------------
def p1_03_14_merge_the_tools():
    def merge_the_tools(string, k):
        for start in range(0, len(string), k):
            chunk = string[start:start + k]
            # dict.fromkeys keeps the first occurrence of each char, in order
            print("".join(dict.fromkeys(chunk)))


    if __name__ == '__main__':
        string, k = input(), int(input())
        merge_the_tools(string, k)

# =========================================================================
# Sets (13 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# -------------------------------------------------------------------------
def p1_04_01_py_introduction_to_sets():
    def average(array):
        distinct = set(array)
        return round(sum(distinct) / len(distinct), 3)


    if __name__ == '__main__':
        n = int(input())
        arr = list(map(int, input().split()))
        result = average(arr)
        print(result)


# -------------------------------------------------------------------------
# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem
# -------------------------------------------------------------------------
def p1_04_02_no_idea():
    n, m = map(int, input().split())
    arr = input().split()
    A = set(input().split())
    B = set(input().split())

    # +1 for each element liked, -1 for each element disliked (O(1) set lookups)
    print(sum((x in A) - (x in B) for x in arr))


# -------------------------------------------------------------------------
# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem
# -------------------------------------------------------------------------
def p1_04_03_symmetric_difference():
    input()
    a = set(map(int, input().split()))
    input()
    b = set(map(int, input().split()))

    for x in sorted(a ^ b):
        print(x)


# -------------------------------------------------------------------------
# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem
# -------------------------------------------------------------------------
def p1_04_04_py_set_add():
    countries = set()
    for _ in range(int(input())):
        countries.add(input().strip())
    print(len(countries))


# -------------------------------------------------------------------------
# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# -------------------------------------------------------------------------
def p1_04_05_py_set_discard_remove_pop():
    n = int(input())
    s = set(map(int, input().split()))

    for _ in range(int(input())):
        cmd, *args = input().split()
        getattr(s, cmd)(*map(int, args))   # pop / remove x / discard x

    print(sum(s))


# -------------------------------------------------------------------------
# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem
# -------------------------------------------------------------------------
def p1_04_06_py_set_union():
    input()
    english = set(input().split())
    input()
    french = set(input().split())

    print(len(english.union(french)))


# -------------------------------------------------------------------------
# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# -------------------------------------------------------------------------
def p1_04_07_py_set_intersection_operation():
    input()
    english = set(input().split())
    input()
    french = set(input().split())

    print(len(english.intersection(french)))


# -------------------------------------------------------------------------
# Set .difference() Operation
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# -------------------------------------------------------------------------
def p1_04_08_py_set_difference_operation():
    input()
    english = set(input().split())
    input()
    french = set(input().split())

    print(len(english.difference(french)))


# -------------------------------------------------------------------------
# Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# -------------------------------------------------------------------------
def p1_04_09_py_set_symmetric_difference_operation():
    input()
    english = set(input().split())
    input()
    french = set(input().split())

    print(len(english.symmetric_difference(french)))


# -------------------------------------------------------------------------
# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem
# -------------------------------------------------------------------------
def p1_04_10_py_set_mutations():
    input()
    A = set(map(int, input().split()))

    for _ in range(int(input())):
        operation, _size = input().split()
        other = set(map(int, input().split()))
        getattr(A, operation)(other)   # update / intersection_update / ...

    print(sum(A))


# -------------------------------------------------------------------------
# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem
# -------------------------------------------------------------------------
def p1_04_11_py_the_captains_room():
    k = int(input())
    rooms = list(map(int, input().split()))

    # every family room appears k times, the captain's room once:
    #   k * sum(distinct) - sum(all) = (k - 1) * captain
    print((k * sum(set(rooms)) - sum(rooms)) // (k - 1))


# -------------------------------------------------------------------------
# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem
# -------------------------------------------------------------------------
def p1_04_12_py_check_subset():
    for _ in range(int(input())):
        input()
        a = set(input().split())
        input()
        b = set(input().split())
        print(a.issubset(b))


# -------------------------------------------------------------------------
# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# -------------------------------------------------------------------------
def p1_04_13_py_check_strict_superset():
    A = set(input().split())
    n = int(input())
    # read all n sets (no early exit, so the whole input is consumed)
    others = [set(input().split()) for _ in range(n)]
    print(all(A > other for other in others))

# =========================================================================
# Collections (8 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem
# -------------------------------------------------------------------------
def p1_05_01_collections_counter():
    from collections import Counter

    input()
    stock = Counter(map(int, input().split()))
    earned = 0
    for _ in range(int(input())):
        size, price = map(int, input().split())
        if stock[size] > 0:
            stock[size] -= 1
            earned += price
    print(earned)


# -------------------------------------------------------------------------
# DefaultDict Tutorial
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# -------------------------------------------------------------------------
def p1_05_02_defaultdict_tutorial():
    from collections import defaultdict

    n, m = map(int, input().split())
    positions = defaultdict(list)
    for i in range(1, n + 1):
        positions[input()].append(i)

    for _ in range(m):
        word = input()
        print(" ".join(map(str, positions[word])) if word in positions else -1)


# -------------------------------------------------------------------------
# Collections.namedtuple()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# -------------------------------------------------------------------------
def p1_05_03_py_collections_namedtuple():
    from collections import namedtuple

    n = int(input())
    Student = namedtuple("Student", input().split())   # columns can be in any order
    students = [Student(*input().split()) for _ in range(n)]
    print(f"{sum(int(s.MARKS) for s in students) / n:.2f}")


# -------------------------------------------------------------------------
# Collections.OrderedDict()
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# -------------------------------------------------------------------------
def p1_05_04_py_collections_ordereddict():
    from collections import OrderedDict

    totals = OrderedDict()
    for _ in range(int(input())):
        *name, price = input().split()
        item = " ".join(name)
        totals[item] = totals.get(item, 0) + int(price)

    for item, total in totals.items():
        print(item, total)


# -------------------------------------------------------------------------
# Word Order
# https://www.hackerrank.com/challenges/word-order/problem
# -------------------------------------------------------------------------
def p1_05_05_word_order():
    from collections import Counter

    words = [input().strip() for _ in range(int(input()))]
    counts = Counter(words)          # keeps first-insertion order (Python 3.7+)
    print(len(counts))
    print(*counts.values())


# -------------------------------------------------------------------------
# Collections.deque()
# https://www.hackerrank.com/challenges/py-collections-deque/problem
# -------------------------------------------------------------------------
def p1_05_06_py_collections_deque():
    from collections import deque

    d = deque()
    for _ in range(int(input())):
        cmd, *args = input().split()
        getattr(d, cmd)(*args)   # append / appendleft / pop / popleft
    print(*d)


# -------------------------------------------------------------------------
# Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem
# -------------------------------------------------------------------------
def p1_05_07_most_commons():
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


# -------------------------------------------------------------------------
# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem
# -------------------------------------------------------------------------
def p1_05_08_piling_up():
    from collections import deque

    for _ in range(int(input())):
        input()
        cubes = deque(map(int, input().split()))
        top = float("inf")
        ok = True
        while cubes:
            # greedily take the larger of the two ends
            cube = cubes.popleft() if cubes[0] >= cubes[-1] else cubes.pop()
            if cube > top:
                ok = False
                break
            top = cube
        print("Yes" if ok else "No")

# =========================================================================
# Date and Time (2 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Calendar Module
# https://www.hackerrank.com/challenges/calendar-module/problem
# -------------------------------------------------------------------------
def p1_06_01_calendar_module():
    import calendar

    month, day, year = map(int, input().split())
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())


# -------------------------------------------------------------------------
# Time Delta
# https://www.hackerrank.com/challenges/python-time-delta/problem
# -------------------------------------------------------------------------
def p1_06_02_python_time_delta():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys
    from datetime import datetime


    # Complete the time_delta function below.
    def time_delta(t1, t2):
        fmt = "%a %d %b %Y %H:%M:%S %z"
        delta = datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)
        return str(int(abs(delta.total_seconds())))


    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        t = int(input())

        for t_itr in range(t):
            t1 = input()

            t2 = input()

            delta = time_delta(t1, t2)

            fptr.write(delta + '\n')

        fptr.close()

# =========================================================================
# Errors and Exceptions (1 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Exceptions
# https://www.hackerrank.com/challenges/exceptions/problem
# -------------------------------------------------------------------------
def p1_07_01_exceptions():
    for _ in range(int(input())):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code:", e)

# =========================================================================
# Built-Ins (3 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Zipped!
# https://www.hackerrank.com/challenges/zipped/problem
# -------------------------------------------------------------------------
def p1_08_01_zipped():
    n, x = map(int, input().split())
    subjects = [map(float, input().split()) for _ in range(x)]

    # zip(*subjects) groups the marks of the same student together
    for marks in zip(*subjects):
        print(f"{sum(marks) / x:.1f}")


# -------------------------------------------------------------------------
# Athlete Sort
# https://www.hackerrank.com/challenges/python-sort-sort/problem
# -------------------------------------------------------------------------
def p1_08_02_python_sort_sort():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys


    if __name__ == '__main__':
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        arr = []

        for _ in range(n):
            arr.append(list(map(int, input().rstrip().split())))

        k = int(input())

        # sorted() is stable: ties keep the input order
        for row in sorted(arr, key=lambda r: r[k]):
            print(*row)


# -------------------------------------------------------------------------
# ginortS
# https://www.hackerrank.com/challenges/ginorts/problem
# -------------------------------------------------------------------------
def p1_08_03_ginorts():
    s = input()

    # order: lowercase < uppercase < odd digits < even digits, then by character
    def rank(c):
        if c.islower():
            return (0, c)
        if c.isupper():
            return (1, c)
        if int(c) % 2 == 1:
            return (2, c)
        return (3, c)

    print("".join(sorted(s, key=rank)))

# =========================================================================
# Python Functionals (1 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Map and Lambda Function
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# -------------------------------------------------------------------------
def p1_09_01_map_and_lambda_expression():
    cube = lambda x: x ** 3


    def fibonacci(n):
        # return a list of the first n fibonacci numbers
        fib = []
        a, b = 0, 1
        for _ in range(n):
            fib.append(a)
            a, b = b, a + b
        return fib


    if __name__ == '__main__':
        n = int(input())
        print(list(map(cube, fibonacci(n))))

# =========================================================================
# Regex and Parsing (17 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Detect Floating Point Number
# https://www.hackerrank.com/challenges/introduction-to-regex/problem
# -------------------------------------------------------------------------
def p1_10_01_introduction_to_regex():
    import re

    # optional sign, any digits, a mandatory dot, at least one digit after it
    pattern = re.compile(r'^[+-]?\d*\.\d+$')
    for _ in range(int(input())):
        print(bool(pattern.match(input().strip())))


# -------------------------------------------------------------------------
# Re.split()
# https://www.hackerrank.com/challenges/re-split/problem
# -------------------------------------------------------------------------
def p1_10_02_re_split():
    regex_pattern = r"[.,]+"	# Do not delete 'r'.

    import re
    print("\n".join(re.split(regex_pattern, input())))


# -------------------------------------------------------------------------
# Group(), Groups() & Groupdict()
# https://www.hackerrank.com/challenges/re-group-groups/problem
# -------------------------------------------------------------------------
def p1_10_03_re_group_groups():
    import re

    # first alphanumeric character followed by itself
    m = re.search(r'([a-zA-Z0-9])\1', input())
    print(m.group(1) if m else -1)


# -------------------------------------------------------------------------
# Re.findall() & Re.finditer()
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# -------------------------------------------------------------------------
def p1_10_04_re_findall_re_finditer():
    import re

    consonants = "qwrtypsdfghjklzxcvbnm"
    vowels = "aeiou"
    pattern = rf'(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])'

    matches = re.findall(pattern, input(), flags=re.IGNORECASE)
    print("\n".join(matches) if matches else -1)


# -------------------------------------------------------------------------
# Re.start() & Re.end()
# https://www.hackerrank.com/challenges/re-start-re-end/problem
# -------------------------------------------------------------------------
def p1_10_05_re_start_re_end():
    import re

    S = input()
    k = input()

    # a zero-width lookahead finds overlapping matches too
    found = False
    for m in re.finditer(r'(?=' + re.escape(k) + r')', S):
        found = True
        print((m.start(), m.start() + len(k) - 1))
    if not found:
        print((-1, -1))


# -------------------------------------------------------------------------
# Regex Substitution
# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
# -------------------------------------------------------------------------
def p1_10_06_re_sub_regex_substitution():
    import re

    # only && / || with a space on both sides
    pattern = re.compile(r'(?<= )(&&|\|\|)(?= )')
    replace = lambda m: "and" if m.group(1) == "&&" else "or"

    for _ in range(int(input())):
        print(pattern.sub(replace, input()))


# -------------------------------------------------------------------------
# Validating Roman Numerals
# https://www.hackerrank.com/challenges/validate-a-roman-number/problem
# -------------------------------------------------------------------------
def p1_10_07_validate_a_roman_number():
    regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

    import re
    print(str(bool(re.match(regex_pattern, input()))))


# -------------------------------------------------------------------------
# Validating phone numbers
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
# -------------------------------------------------------------------------
def p1_10_08_validating_the_phone_number():
    import re

    for _ in range(int(input())):
        print("YES" if re.match(r'^[789]\d{9}$', input().strip()) else "NO")


# -------------------------------------------------------------------------
# Validating and Parsing Email Addresses
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# -------------------------------------------------------------------------
def p1_10_09_validating_named_email_addresses():
    import re
    import email.utils

    # username: starts with a letter, then letters/digits/-/./_ ; domain: letters ;
    # extension: 1-3 letters
    pattern = re.compile(r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

    for _ in range(int(input())):
        line = input().strip()
        name, addr = email.utils.parseaddr(line)
        if pattern.match(addr):
            print(line)


# -------------------------------------------------------------------------
# Hex Color Code
# https://www.hackerrank.com/challenges/hex-color-code/problem
# -------------------------------------------------------------------------
def p1_10_10_hex_color_code():
    import re

    css = "\n".join(input() for _ in range(int(input())))

    # colours only appear inside { ... } blocks (selectors like #BED are outside)
    hex_color = re.compile(r'#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?![0-9a-zA-Z])')
    for block in re.findall(r'\{([^}]*)\}', css):
        for color in hex_color.findall(block):
            print(color)


# -------------------------------------------------------------------------
# HTML Parser - Part 1
# https://www.hackerrank.com/challenges/html-parser-part-1/problem
# -------------------------------------------------------------------------
def p1_10_11_html_parser_part_1():
    from html.parser import HTMLParser


    class MyHTMLParser(HTMLParser):
        def _print_attrs(self, attrs):
            for name, value in attrs:
                print("->", name, ">", value)

        def handle_starttag(self, tag, attrs):
            print("Start :", tag)
            self._print_attrs(attrs)

        def handle_endtag(self, tag):
            print("End   :", tag)

        def handle_startendtag(self, tag, attrs):
            print("Empty :", tag)
            self._print_attrs(attrs)


    parser = MyHTMLParser()
    parser.feed("\n".join(input() for _ in range(int(input()))))
    parser.close()


# -------------------------------------------------------------------------
# HTML Parser - Part 2
# https://www.hackerrank.com/challenges/html-parser-part-2/problem
# -------------------------------------------------------------------------
def p1_10_12_html_parser_part_2():
    from html.parser import HTMLParser


    class MyHTMLParser(HTMLParser):
        def handle_comment(self, data):
            if "\n" in data:
                print(">>> Multi-line Comment")
            else:
                print(">>> Single-line Comment")
            print(data)

        def handle_data(self, data):
            if data != "\n":
                print(">>> Data")
                print(data)


    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()


# -------------------------------------------------------------------------
# Detect HTML Tags, Attributes and Attribute Values
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
# -------------------------------------------------------------------------
def p1_10_13_detect_html_tags_attributes_and_attribute_values():
    from html.parser import HTMLParser


    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print(tag)
            for name, value in attrs:
                print("->", name, ">", value)

        # self-closing tags (<br />) are reported the same way
        handle_startendtag = handle_starttag


    parser = MyHTMLParser()
    parser.feed("\n".join(input() for _ in range(int(input()))))
    parser.close()


# -------------------------------------------------------------------------
# Validating UID
# https://www.hackerrank.com/challenges/validating-uid/problem
# -------------------------------------------------------------------------
def p1_10_14_validating_uid():
    def is_valid(uid):
        return (len(uid) == 10
                and uid.isalnum()
                and len(set(uid)) == 10                       # no repeated characters
                and sum(c.isupper() for c in uid) >= 2
                and sum(c.isdigit() for c in uid) >= 3)


    for _ in range(int(input())):
        print("Valid" if is_valid(input().strip()) else "Invalid")


# -------------------------------------------------------------------------
# Validating Credit Card Numbers
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# -------------------------------------------------------------------------
def p1_10_15_validating_credit_card_number():
    import re

    # starts with 4/5/6, 16 digits, optionally in groups of 4 separated by "-"
    fmt = re.compile(r'^[456]\d{3}(-?\d{4}){3}$')
    # 4 or more consecutive repeated digits
    repeated = re.compile(r'(\d)\1{3}')

    for _ in range(int(input())):
        card = input().strip()
        ok = fmt.match(card) and not repeated.search(card.replace("-", ""))
        print("Valid" if ok else "Invalid")


# -------------------------------------------------------------------------
# Validating Postal Codes
# https://www.hackerrank.com/challenges/validating-postalcode/problem
# -------------------------------------------------------------------------
def p1_10_16_validating_postalcode():
    regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


    import re
    P = input()

    print (bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# -------------------------------------------------------------------------
# Matrix Script
# https://www.hackerrank.com/challenges/matrix-script/problem
# -------------------------------------------------------------------------
def p1_10_17_matrix_script():
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

# =========================================================================
# XML (2 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# XML 1 - Find the Score
# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
# -------------------------------------------------------------------------
def p1_11_01_xml_1_find_the_score():
    import sys
    import xml.etree.ElementTree as etree

    def get_attr_number(node):
        # attributes of this node plus those of all its descendants
        return len(node.attrib) + sum(get_attr_number(child) for child in node)

    if __name__ == '__main__':
        sys.stdin.readline()
        xml = sys.stdin.read()
        tree = etree.ElementTree(etree.fromstring(xml))
        root = tree.getroot()
        print(get_attr_number(root))


# -------------------------------------------------------------------------
# XML2 - Find the Maximum Depth
# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
# -------------------------------------------------------------------------
def p1_11_02_xml2_find_the_maximum_depth():
    global maxdepth
    import xml.etree.ElementTree as etree

    maxdepth = 0
    def depth(elem, level):
        global maxdepth
        level += 1                       # the root is called with level -1 -> 0
        maxdepth = max(maxdepth, level)
        for child in elem:
            depth(child, level)

    if __name__ == '__main__':
        n = int(input())
        xml = ""
        for i in range(n):
            xml =  xml + input() + "\n"
        tree = etree.ElementTree(etree.fromstring(xml))
        depth(tree.getroot(), -1)
        print(maxdepth)

# =========================================================================
# Closures and Decorators (2 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Standardize Mobile Number Using Decorators
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
# -------------------------------------------------------------------------
def p1_12_01_standardize_mobile_number_using_decorators():
    def wrapper(f):
        def fun(l):
            # keep the last 10 digits, drop any +91 / 91 / 0 prefix
            f(["+91 " + num[-10:-5] + " " + num[-5:] for num in l])
        return fun

    @wrapper
    def sort_phone(l):
        print(*sorted(l), sep='\n')

    if __name__ == '__main__':
        l = [input() for _ in range(int(input()))]
        sort_phone(l)


# -------------------------------------------------------------------------
# Decorators 2 - Name Directory
# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem
# -------------------------------------------------------------------------
def p1_12_02_decorators_2_name_directory():
    import operator

    def person_lister(f):
        def inner(people):
            # sort by age (as an integer); sorted() is stable for equal ages
            return [f(person) for person in sorted(people, key=lambda p: int(p[2]))]
        return inner

    @person_lister
    def name_format(person):
        return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

    if __name__ == '__main__':
        people = [input().split() for i in range(int(input()))]
        print(*name_format(people), sep='\n')

# =========================================================================
# Numpy (15 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Arrays
# https://www.hackerrank.com/challenges/np-arrays/problem
# -------------------------------------------------------------------------
def p1_13_01_np_arrays():
    import numpy

    numpy.set_printoptions(legacy='1.13')

    def arrays(arr):
        # reversed, as floats
        return numpy.array(arr[::-1], float)

    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)


# -------------------------------------------------------------------------
# Shape and Reshape
# https://www.hackerrank.com/challenges/np-shape-reshape/problem
# -------------------------------------------------------------------------
def p1_13_02_np_shape_reshape():
    import numpy

    arr = numpy.array(input().split(), int)
    print(numpy.reshape(arr, (3, 3)))


# -------------------------------------------------------------------------
# Transpose and Flatten
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# -------------------------------------------------------------------------
def p1_13_03_np_transpose_and_flatten():
    import numpy

    n, m = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(n)], int)
    print(numpy.transpose(arr))
    print(arr.flatten())


# -------------------------------------------------------------------------
# Concatenate
# https://www.hackerrank.com/challenges/np-concatenate/problem
# -------------------------------------------------------------------------
def p1_13_04_np_concatenate():
    import numpy

    n, m, p = map(int, input().split())
    a = numpy.array([input().split() for _ in range(n)], int)
    b = numpy.array([input().split() for _ in range(m)], int)
    print(numpy.concatenate((a, b), axis=0))


# -------------------------------------------------------------------------
# Zeros and Ones
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
# -------------------------------------------------------------------------
def p1_13_05_np_zeros_and_ones():
    import numpy

    shape = tuple(map(int, input().split()))
    print(numpy.zeros(shape, dtype=int))
    print(numpy.ones(shape, dtype=int))


# -------------------------------------------------------------------------
# Eye and Identity
# https://www.hackerrank.com/challenges/np-eye-and-identity/problem
# -------------------------------------------------------------------------
def p1_13_06_np_eye_and_identity():
    import numpy

    numpy.set_printoptions(legacy='1.13')

    n, m = map(int, input().split())
    print(numpy.eye(n, m))


# -------------------------------------------------------------------------
# Array Mathematics
# https://www.hackerrank.com/challenges/np-array-mathematics/problem
# -------------------------------------------------------------------------
def p1_13_07_np_array_mathematics():
    import numpy

    n, m = map(int, input().split())
    a = numpy.array([input().split() for _ in range(n)], int)
    b = numpy.array([input().split() for _ in range(n)], int)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)


# -------------------------------------------------------------------------
# Floor, Ceil and Rint
# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
# -------------------------------------------------------------------------
def p1_13_08_floor_ceil_and_rint():
    import numpy

    numpy.set_printoptions(legacy='1.13')

    a = numpy.array(input().split(), float)
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))


# -------------------------------------------------------------------------
# Sum and Prod
# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# -------------------------------------------------------------------------
def p1_13_09_np_sum_and_prod():
    import numpy

    n, m = map(int, input().split())
    a = numpy.array([input().split() for _ in range(n)], int)
    print(numpy.prod(numpy.sum(a, axis=0)))


# -------------------------------------------------------------------------
# Min and Max
# https://www.hackerrank.com/challenges/np-min-and-max/problem
# -------------------------------------------------------------------------
def p1_13_10_np_min_and_max():
    import numpy

    n, m = map(int, input().split())
    a = numpy.array([input().split() for _ in range(n)], int)
    print(numpy.max(numpy.min(a, axis=1)))


# -------------------------------------------------------------------------
# Mean, Var, and Std
# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# -------------------------------------------------------------------------
def p1_13_11_np_mean_var_and_std():
    import numpy

    numpy.set_printoptions(legacy='1.13')

    n, m = map(int, input().split())
    a = numpy.array([input().split() for _ in range(n)], int)
    print(numpy.mean(a, axis=1))
    print(numpy.var(a, axis=0))
    print(numpy.std(a))


# -------------------------------------------------------------------------
# Dot and Cross
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
# -------------------------------------------------------------------------
def p1_13_12_np_dot_and_cross():
    import numpy

    n = int(input())
    a = numpy.array([input().split() for _ in range(n)], int)
    b = numpy.array([input().split() for _ in range(n)], int)
    print(numpy.dot(a, b))


# -------------------------------------------------------------------------
# Inner and Outer
# https://www.hackerrank.com/challenges/np-inner-and-outer/problem
# -------------------------------------------------------------------------
def p1_13_13_np_inner_and_outer():
    import numpy

    a = numpy.array(input().split(), int)
    b = numpy.array(input().split(), int)
    print(numpy.inner(a, b))
    print(numpy.outer(a, b))


# -------------------------------------------------------------------------
# Polynomials
# https://www.hackerrank.com/challenges/np-polynomials/problem
# -------------------------------------------------------------------------
def p1_13_14_np_polynomials():
    import numpy

    coefficients = list(map(float, input().split()))
    x = float(input())
    print(numpy.polyval(coefficients, x))


# -------------------------------------------------------------------------
# Linear Algebra
# https://www.hackerrank.com/challenges/np-linear-algebra/problem
# -------------------------------------------------------------------------
def p1_13_15_np_linear_algebra():
    import numpy

    n = int(input())
    a = numpy.array([input().split() for _ in range(n)], float)
    print(round(numpy.linalg.det(a), 2))

###########################################################################
#                          PROBLEM 2 - Algorithms                         #
###########################################################################

# =========================================================================
# Problem 2 - Algorithms (6 challenges)
# =========================================================================


# -------------------------------------------------------------------------
# Birthday Cake Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# -------------------------------------------------------------------------
def p2_01_birthday_cake_candles():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'birthdayCakeCandles' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts INTEGER_ARRAY candles as parameter.
    #

    def birthdayCakeCandles(candles):
        # single pass: track the tallest height and how many times it appears
        tallest, count = 0, 0
        for h in candles:
            if h > tallest:
                tallest, count = h, 1
            elif h == tallest:
                count += 1
        return count

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        candles_count = int(input().strip())

        candles = list(map(int, input().rstrip().split()))

        result = birthdayCakeCandles(candles)

        fptr.write(str(result) + '\n')

        fptr.close()


# -------------------------------------------------------------------------
# Number Line Jumps (Kangaroo)
# https://www.hackerrank.com/challenges/kangaroo/problem
# -------------------------------------------------------------------------
def p2_02_kangaroo():
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


# -------------------------------------------------------------------------
# Viral Advertising
# https://www.hackerrank.com/challenges/strange-advertising/problem
# -------------------------------------------------------------------------
def p2_03_strange_advertising():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'viralAdvertising' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts INTEGER n as parameter.
    #

    def viralAdvertising(n):
        shared, cumulative = 5, 0
        for _ in range(n):
            liked = shared // 2          # half the recipients like it
            cumulative += liked
            shared = liked * 3           # each one shares with 3 friends
        return cumulative

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input().strip())

        result = viralAdvertising(n)

        fptr.write(str(result) + '\n')

        fptr.close()


# -------------------------------------------------------------------------
# Recursive Digit Sum
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem
# -------------------------------------------------------------------------
def p2_04_recursive_digit_sum():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'superDigit' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. STRING n
    #  2. INTEGER k
    #

    def superDigit(n, k):
        # the digit sum of n repeated k times is k * digit_sum(n), so we never
        # need to build the (possibly 10^5 * 10^5 digit) string p
        total = sum(int(d) for d in n) * k
        if total < 10:
            return total
        return superDigit(str(total), 1)

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        first_multiple_input = input().rstrip().split()

        n = first_multiple_input[0]

        k = int(first_multiple_input[1])

        result = superDigit(n, k)

        fptr.write(str(result) + '\n')

        fptr.close()


# -------------------------------------------------------------------------
# Insertion Sort - Part 1
# https://www.hackerrank.com/challenges/insertionsort1/problem
# -------------------------------------------------------------------------
def p2_05_insertionsort1():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'insertionSort1' function below.
    #
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. INTEGER_ARRAY arr
    #

    def insertionSort1(n, arr):
        value = arr[-1]          # the unsorted element, stored aside
        i = n - 2
        # shift every larger element one cell to the right, printing each step
        while i >= 0 and arr[i] > value:
            arr[i + 1] = arr[i]
            print(*arr)
            i -= 1
        arr[i + 1] = value
        print(*arr)

    if __name__ == '__main__':
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        insertionSort1(n, arr)


# -------------------------------------------------------------------------
# Insertion Sort - Part 2
# https://www.hackerrank.com/challenges/insertionsort2/problem
# -------------------------------------------------------------------------
def p2_06_insertionsort2():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'insertionSort2' function below.
    #
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. INTEGER_ARRAY arr
    #

    def insertionSort2(n, arr):
        # grow a sorted prefix; insert arr[i] into it, print after every pass
        for i in range(1, n):
            value = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > value:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = value
            print(*arr)

    if __name__ == '__main__':
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        insertionSort2(n, arr)


# =========================================================================
# Command-line runner
# =========================================================================
SOLUTIONS = {
    'p1_01_01_py_hello_world': p1_01_01_py_hello_world,
    'p1_01_02_py_if_else': p1_01_02_py_if_else,
    'p1_01_03_python_arithmetic_operators': p1_01_03_python_arithmetic_operators,
    'p1_01_04_python_division': p1_01_04_python_division,
    'p1_01_05_python_loops': p1_01_05_python_loops,
    'p1_01_06_write_a_function': p1_01_06_write_a_function,
    'p1_01_07_python_print': p1_01_07_python_print,
    'p1_02_01_list_comprehensions': p1_02_01_list_comprehensions,
    'p1_02_02_find_second_maximum_number_in_a_list': p1_02_02_find_second_maximum_number_in_a_list,
    'p1_02_03_nested_list': p1_02_03_nested_list,
    'p1_02_04_finding_the_percentage': p1_02_04_finding_the_percentage,
    'p1_02_05_python_lists': p1_02_05_python_lists,
    'p1_02_06_python_tuples': p1_02_06_python_tuples,
    'p1_03_01_swap_case': p1_03_01_swap_case,
    'p1_03_02_python_string_split_and_join': p1_03_02_python_string_split_and_join,
    'p1_03_03_whats_your_name': p1_03_03_whats_your_name,
    'p1_03_04_python_mutations': p1_03_04_python_mutations,
    'p1_03_05_find_a_string': p1_03_05_find_a_string,
    'p1_03_06_string_validators': p1_03_06_string_validators,
    'p1_03_07_text_alignment': p1_03_07_text_alignment,
    'p1_03_08_text_wrap': p1_03_08_text_wrap,
    'p1_03_09_designer_door_mat': p1_03_09_designer_door_mat,
    'p1_03_10_python_string_formatting': p1_03_10_python_string_formatting,
    'p1_03_11_alphabet_rangoli': p1_03_11_alphabet_rangoli,
    'p1_03_12_capitalize': p1_03_12_capitalize,
    'p1_03_13_the_minion_game': p1_03_13_the_minion_game,
    'p1_03_14_merge_the_tools': p1_03_14_merge_the_tools,
    'p1_04_01_py_introduction_to_sets': p1_04_01_py_introduction_to_sets,
    'p1_04_02_no_idea': p1_04_02_no_idea,
    'p1_04_03_symmetric_difference': p1_04_03_symmetric_difference,
    'p1_04_04_py_set_add': p1_04_04_py_set_add,
    'p1_04_05_py_set_discard_remove_pop': p1_04_05_py_set_discard_remove_pop,
    'p1_04_06_py_set_union': p1_04_06_py_set_union,
    'p1_04_07_py_set_intersection_operation': p1_04_07_py_set_intersection_operation,
    'p1_04_08_py_set_difference_operation': p1_04_08_py_set_difference_operation,
    'p1_04_09_py_set_symmetric_difference_operation': p1_04_09_py_set_symmetric_difference_operation,
    'p1_04_10_py_set_mutations': p1_04_10_py_set_mutations,
    'p1_04_11_py_the_captains_room': p1_04_11_py_the_captains_room,
    'p1_04_12_py_check_subset': p1_04_12_py_check_subset,
    'p1_04_13_py_check_strict_superset': p1_04_13_py_check_strict_superset,
    'p1_05_01_collections_counter': p1_05_01_collections_counter,
    'p1_05_02_defaultdict_tutorial': p1_05_02_defaultdict_tutorial,
    'p1_05_03_py_collections_namedtuple': p1_05_03_py_collections_namedtuple,
    'p1_05_04_py_collections_ordereddict': p1_05_04_py_collections_ordereddict,
    'p1_05_05_word_order': p1_05_05_word_order,
    'p1_05_06_py_collections_deque': p1_05_06_py_collections_deque,
    'p1_05_07_most_commons': p1_05_07_most_commons,
    'p1_05_08_piling_up': p1_05_08_piling_up,
    'p1_06_01_calendar_module': p1_06_01_calendar_module,
    'p1_06_02_python_time_delta': p1_06_02_python_time_delta,
    'p1_07_01_exceptions': p1_07_01_exceptions,
    'p1_08_01_zipped': p1_08_01_zipped,
    'p1_08_02_python_sort_sort': p1_08_02_python_sort_sort,
    'p1_08_03_ginorts': p1_08_03_ginorts,
    'p1_09_01_map_and_lambda_expression': p1_09_01_map_and_lambda_expression,
    'p1_10_01_introduction_to_regex': p1_10_01_introduction_to_regex,
    'p1_10_02_re_split': p1_10_02_re_split,
    'p1_10_03_re_group_groups': p1_10_03_re_group_groups,
    'p1_10_04_re_findall_re_finditer': p1_10_04_re_findall_re_finditer,
    'p1_10_05_re_start_re_end': p1_10_05_re_start_re_end,
    'p1_10_06_re_sub_regex_substitution': p1_10_06_re_sub_regex_substitution,
    'p1_10_07_validate_a_roman_number': p1_10_07_validate_a_roman_number,
    'p1_10_08_validating_the_phone_number': p1_10_08_validating_the_phone_number,
    'p1_10_09_validating_named_email_addresses': p1_10_09_validating_named_email_addresses,
    'p1_10_10_hex_color_code': p1_10_10_hex_color_code,
    'p1_10_11_html_parser_part_1': p1_10_11_html_parser_part_1,
    'p1_10_12_html_parser_part_2': p1_10_12_html_parser_part_2,
    'p1_10_13_detect_html_tags_attributes_and_attribute_values': p1_10_13_detect_html_tags_attributes_and_attribute_values,
    'p1_10_14_validating_uid': p1_10_14_validating_uid,
    'p1_10_15_validating_credit_card_number': p1_10_15_validating_credit_card_number,
    'p1_10_16_validating_postalcode': p1_10_16_validating_postalcode,
    'p1_10_17_matrix_script': p1_10_17_matrix_script,
    'p1_11_01_xml_1_find_the_score': p1_11_01_xml_1_find_the_score,
    'p1_11_02_xml2_find_the_maximum_depth': p1_11_02_xml2_find_the_maximum_depth,
    'p1_12_01_standardize_mobile_number_using_decorators': p1_12_01_standardize_mobile_number_using_decorators,
    'p1_12_02_decorators_2_name_directory': p1_12_02_decorators_2_name_directory,
    'p1_13_01_np_arrays': p1_13_01_np_arrays,
    'p1_13_02_np_shape_reshape': p1_13_02_np_shape_reshape,
    'p1_13_03_np_transpose_and_flatten': p1_13_03_np_transpose_and_flatten,
    'p1_13_04_np_concatenate': p1_13_04_np_concatenate,
    'p1_13_05_np_zeros_and_ones': p1_13_05_np_zeros_and_ones,
    'p1_13_06_np_eye_and_identity': p1_13_06_np_eye_and_identity,
    'p1_13_07_np_array_mathematics': p1_13_07_np_array_mathematics,
    'p1_13_08_floor_ceil_and_rint': p1_13_08_floor_ceil_and_rint,
    'p1_13_09_np_sum_and_prod': p1_13_09_np_sum_and_prod,
    'p1_13_10_np_min_and_max': p1_13_10_np_min_and_max,
    'p1_13_11_np_mean_var_and_std': p1_13_11_np_mean_var_and_std,
    'p1_13_12_np_dot_and_cross': p1_13_12_np_dot_and_cross,
    'p1_13_13_np_inner_and_outer': p1_13_13_np_inner_and_outer,
    'p1_13_14_np_polynomials': p1_13_14_np_polynomials,
    'p1_13_15_np_linear_algebra': p1_13_15_np_linear_algebra,
    'p2_01_birthday_cake_candles': p2_01_birthday_cake_candles,
    'p2_02_kangaroo': p2_02_kangaroo,
    'p2_03_strange_advertising': p2_03_strange_advertising,
    'p2_04_recursive_digit_sum': p2_04_recursive_digit_sum,
    'p2_05_insertionsort1': p2_05_insertionsort1,
    'p2_06_insertionsort2': p2_06_insertionsort2
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("list", "-h", "--help"):
        for name, (title, url) in SOLUTIONS_INFO.items():
            print(f"{name:<55} {title}")
        return
    name = sys.argv[1]
    if name not in SOLUTIONS:
        sys.exit(f"Unknown solution {name!r}. Run `python scripts.py list`.")
    tmp = None
    if "OUTPUT_PATH" not in os.environ:
        fd, tmp = tempfile.mkstemp(suffix=".out")
        os.close(fd)
        os.environ["OUTPUT_PATH"] = tmp
    try:
        SOLUTIONS[name]()
    finally:
        if tmp is not None:
            sys.stdout.flush()
            with open(tmp) as f:
                sys.stdout.write(f.read())
            os.remove(tmp)


SOLUTIONS_INFO = {
    'p1_01_01_py_hello_world': ('Say "Hello, World!" With Python', 'https://www.hackerrank.com/challenges/py-hello-world/problem'),
    'p1_01_02_py_if_else': ('Python If-Else', 'https://www.hackerrank.com/challenges/py-if-else/problem'),
    'p1_01_03_python_arithmetic_operators': ('Arithmetic Operators', 'https://www.hackerrank.com/challenges/python-arithmetic-operators/problem'),
    'p1_01_04_python_division': ('Python: Division', 'https://www.hackerrank.com/challenges/python-division/problem'),
    'p1_01_05_python_loops': ('Loops', 'https://www.hackerrank.com/challenges/python-loops/problem'),
    'p1_01_06_write_a_function': ('Write a function', 'https://www.hackerrank.com/challenges/write-a-function/problem'),
    'p1_01_07_python_print': ('Print Function', 'https://www.hackerrank.com/challenges/python-print/problem'),
    'p1_02_01_list_comprehensions': ('List Comprehensions', 'https://www.hackerrank.com/challenges/list-comprehensions/problem'),
    'p1_02_02_find_second_maximum_number_in_a_list': ('Find the Runner-Up Score!', 'https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem'),
    'p1_02_03_nested_list': ('Nested Lists', 'https://www.hackerrank.com/challenges/nested-list/problem'),
    'p1_02_04_finding_the_percentage': ('Finding the percentage', 'https://www.hackerrank.com/challenges/finding-the-percentage/problem'),
    'p1_02_05_python_lists': ('Lists', 'https://www.hackerrank.com/challenges/python-lists/problem'),
    'p1_02_06_python_tuples': ('Tuples', 'https://www.hackerrank.com/challenges/python-tuples/problem'),
    'p1_03_01_swap_case': ('sWAP cASE', 'https://www.hackerrank.com/challenges/swap-case/problem'),
    'p1_03_02_python_string_split_and_join': ('String Split and Join', 'https://www.hackerrank.com/challenges/python-string-split-and-join/problem'),
    'p1_03_03_whats_your_name': ("What's Your Name?", 'https://www.hackerrank.com/challenges/whats-your-name/problem'),
    'p1_03_04_python_mutations': ('Mutations', 'https://www.hackerrank.com/challenges/python-mutations/problem'),
    'p1_03_05_find_a_string': ('Find a string', 'https://www.hackerrank.com/challenges/find-a-string/problem'),
    'p1_03_06_string_validators': ('String Validators', 'https://www.hackerrank.com/challenges/string-validators/problem'),
    'p1_03_07_text_alignment': ('Text Alignment', 'https://www.hackerrank.com/challenges/text-alignment/problem'),
    'p1_03_08_text_wrap': ('Text Wrap', 'https://www.hackerrank.com/challenges/text-wrap/problem'),
    'p1_03_09_designer_door_mat': ('Designer Door Mat', 'https://www.hackerrank.com/challenges/designer-door-mat/problem'),
    'p1_03_10_python_string_formatting': ('String Formatting', 'https://www.hackerrank.com/challenges/python-string-formatting/problem'),
    'p1_03_11_alphabet_rangoli': ('Alphabet Rangoli', 'https://www.hackerrank.com/challenges/alphabet-rangoli/problem'),
    'p1_03_12_capitalize': ('Capitalize!', 'https://www.hackerrank.com/challenges/capitalize/problem'),
    'p1_03_13_the_minion_game': ('The Minion Game', 'https://www.hackerrank.com/challenges/the-minion-game/problem'),
    'p1_03_14_merge_the_tools': ('Merge the Tools!', 'https://www.hackerrank.com/challenges/merge-the-tools/problem'),
    'p1_04_01_py_introduction_to_sets': ('Introduction to Sets', 'https://www.hackerrank.com/challenges/py-introduction-to-sets/problem'),
    'p1_04_02_no_idea': ('No Idea!', 'https://www.hackerrank.com/challenges/no-idea/problem'),
    'p1_04_03_symmetric_difference': ('Symmetric Difference', 'https://www.hackerrank.com/challenges/symmetric-difference/problem'),
    'p1_04_04_py_set_add': ('Set .add()', 'https://www.hackerrank.com/challenges/py-set-add/problem'),
    'p1_04_05_py_set_discard_remove_pop': ('Set .discard(), .remove() & .pop()', 'https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem'),
    'p1_04_06_py_set_union': ('Set .union() Operation', 'https://www.hackerrank.com/challenges/py-set-union/problem'),
    'p1_04_07_py_set_intersection_operation': ('Set .intersection() Operation', 'https://www.hackerrank.com/challenges/py-set-intersection-operation/problem'),
    'p1_04_08_py_set_difference_operation': ('Set .difference() Operation', 'https://www.hackerrank.com/challenges/py-set-difference-operation/problem'),
    'p1_04_09_py_set_symmetric_difference_operation': ('Set .symmetric_difference() Operation', 'https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem'),
    'p1_04_10_py_set_mutations': ('Set Mutations', 'https://www.hackerrank.com/challenges/py-set-mutations/problem'),
    'p1_04_11_py_the_captains_room': ("The Captain's Room", 'https://www.hackerrank.com/challenges/py-the-captains-room/problem'),
    'p1_04_12_py_check_subset': ('Check Subset', 'https://www.hackerrank.com/challenges/py-check-subset/problem'),
    'p1_04_13_py_check_strict_superset': ('Check Strict Superset', 'https://www.hackerrank.com/challenges/py-check-strict-superset/problem'),
    'p1_05_01_collections_counter': ('collections.Counter()', 'https://www.hackerrank.com/challenges/collections-counter/problem'),
    'p1_05_02_defaultdict_tutorial': ('DefaultDict Tutorial', 'https://www.hackerrank.com/challenges/defaultdict-tutorial/problem'),
    'p1_05_03_py_collections_namedtuple': ('Collections.namedtuple()', 'https://www.hackerrank.com/challenges/py-collections-namedtuple/problem'),
    'p1_05_04_py_collections_ordereddict': ('Collections.OrderedDict()', 'https://www.hackerrank.com/challenges/py-collections-ordereddict/problem'),
    'p1_05_05_word_order': ('Word Order', 'https://www.hackerrank.com/challenges/word-order/problem'),
    'p1_05_06_py_collections_deque': ('Collections.deque()', 'https://www.hackerrank.com/challenges/py-collections-deque/problem'),
    'p1_05_07_most_commons': ('Company Logo', 'https://www.hackerrank.com/challenges/most-commons/problem'),
    'p1_05_08_piling_up': ('Piling Up!', 'https://www.hackerrank.com/challenges/piling-up/problem'),
    'p1_06_01_calendar_module': ('Calendar Module', 'https://www.hackerrank.com/challenges/calendar-module/problem'),
    'p1_06_02_python_time_delta': ('Time Delta', 'https://www.hackerrank.com/challenges/python-time-delta/problem'),
    'p1_07_01_exceptions': ('Exceptions', 'https://www.hackerrank.com/challenges/exceptions/problem'),
    'p1_08_01_zipped': ('Zipped!', 'https://www.hackerrank.com/challenges/zipped/problem'),
    'p1_08_02_python_sort_sort': ('Athlete Sort', 'https://www.hackerrank.com/challenges/python-sort-sort/problem'),
    'p1_08_03_ginorts': ('ginortS', 'https://www.hackerrank.com/challenges/ginorts/problem'),
    'p1_09_01_map_and_lambda_expression': ('Map and Lambda Function', 'https://www.hackerrank.com/challenges/map-and-lambda-expression/problem'),
    'p1_10_01_introduction_to_regex': ('Detect Floating Point Number', 'https://www.hackerrank.com/challenges/introduction-to-regex/problem'),
    'p1_10_02_re_split': ('Re.split()', 'https://www.hackerrank.com/challenges/re-split/problem'),
    'p1_10_03_re_group_groups': ('Group(), Groups() & Groupdict()', 'https://www.hackerrank.com/challenges/re-group-groups/problem'),
    'p1_10_04_re_findall_re_finditer': ('Re.findall() & Re.finditer()', 'https://www.hackerrank.com/challenges/re-findall-re-finditer/problem'),
    'p1_10_05_re_start_re_end': ('Re.start() & Re.end()', 'https://www.hackerrank.com/challenges/re-start-re-end/problem'),
    'p1_10_06_re_sub_regex_substitution': ('Regex Substitution', 'https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem'),
    'p1_10_07_validate_a_roman_number': ('Validating Roman Numerals', 'https://www.hackerrank.com/challenges/validate-a-roman-number/problem'),
    'p1_10_08_validating_the_phone_number': ('Validating phone numbers', 'https://www.hackerrank.com/challenges/validating-the-phone-number/problem'),
    'p1_10_09_validating_named_email_addresses': ('Validating and Parsing Email Addresses', 'https://www.hackerrank.com/challenges/validating-named-email-addresses/problem'),
    'p1_10_10_hex_color_code': ('Hex Color Code', 'https://www.hackerrank.com/challenges/hex-color-code/problem'),
    'p1_10_11_html_parser_part_1': ('HTML Parser - Part 1', 'https://www.hackerrank.com/challenges/html-parser-part-1/problem'),
    'p1_10_12_html_parser_part_2': ('HTML Parser - Part 2', 'https://www.hackerrank.com/challenges/html-parser-part-2/problem'),
    'p1_10_13_detect_html_tags_attributes_and_attribute_values': ('Detect HTML Tags, Attributes and Attribute Values', 'https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem'),
    'p1_10_14_validating_uid': ('Validating UID', 'https://www.hackerrank.com/challenges/validating-uid/problem'),
    'p1_10_15_validating_credit_card_number': ('Validating Credit Card Numbers', 'https://www.hackerrank.com/challenges/validating-credit-card-number/problem'),
    'p1_10_16_validating_postalcode': ('Validating Postal Codes', 'https://www.hackerrank.com/challenges/validating-postalcode/problem'),
    'p1_10_17_matrix_script': ('Matrix Script', 'https://www.hackerrank.com/challenges/matrix-script/problem'),
    'p1_11_01_xml_1_find_the_score': ('XML 1 - Find the Score', 'https://www.hackerrank.com/challenges/xml-1-find-the-score/problem'),
    'p1_11_02_xml2_find_the_maximum_depth': ('XML2 - Find the Maximum Depth', 'https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem'),
    'p1_12_01_standardize_mobile_number_using_decorators': ('Standardize Mobile Number Using Decorators', 'https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem'),
    'p1_12_02_decorators_2_name_directory': ('Decorators 2 - Name Directory', 'https://www.hackerrank.com/challenges/decorators-2-name-directory/problem'),
    'p1_13_01_np_arrays': ('Arrays', 'https://www.hackerrank.com/challenges/np-arrays/problem'),
    'p1_13_02_np_shape_reshape': ('Shape and Reshape', 'https://www.hackerrank.com/challenges/np-shape-reshape/problem'),
    'p1_13_03_np_transpose_and_flatten': ('Transpose and Flatten', 'https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem'),
    'p1_13_04_np_concatenate': ('Concatenate', 'https://www.hackerrank.com/challenges/np-concatenate/problem'),
    'p1_13_05_np_zeros_and_ones': ('Zeros and Ones', 'https://www.hackerrank.com/challenges/np-zeros-and-ones/problem'),
    'p1_13_06_np_eye_and_identity': ('Eye and Identity', 'https://www.hackerrank.com/challenges/np-eye-and-identity/problem'),
    'p1_13_07_np_array_mathematics': ('Array Mathematics', 'https://www.hackerrank.com/challenges/np-array-mathematics/problem'),
    'p1_13_08_floor_ceil_and_rint': ('Floor, Ceil and Rint', 'https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem'),
    'p1_13_09_np_sum_and_prod': ('Sum and Prod', 'https://www.hackerrank.com/challenges/np-sum-and-prod/problem'),
    'p1_13_10_np_min_and_max': ('Min and Max', 'https://www.hackerrank.com/challenges/np-min-and-max/problem'),
    'p1_13_11_np_mean_var_and_std': ('Mean, Var, and Std', 'https://www.hackerrank.com/challenges/np-mean-var-and-std/problem'),
    'p1_13_12_np_dot_and_cross': ('Dot and Cross', 'https://www.hackerrank.com/challenges/np-dot-and-cross/problem'),
    'p1_13_13_np_inner_and_outer': ('Inner and Outer', 'https://www.hackerrank.com/challenges/np-inner-and-outer/problem'),
    'p1_13_14_np_polynomials': ('Polynomials', 'https://www.hackerrank.com/challenges/np-polynomials/problem'),
    'p1_13_15_np_linear_algebra': ('Linear Algebra', 'https://www.hackerrank.com/challenges/np-linear-algebra/problem'),
    'p2_01_birthday_cake_candles': ('Birthday Cake Candles', 'https://www.hackerrank.com/challenges/birthday-cake-candles/problem'),
    'p2_02_kangaroo': ('Number Line Jumps (Kangaroo)', 'https://www.hackerrank.com/challenges/kangaroo/problem'),
    'p2_03_strange_advertising': ('Viral Advertising', 'https://www.hackerrank.com/challenges/strange-advertising/problem'),
    'p2_04_recursive_digit_sum': ('Recursive Digit Sum', 'https://www.hackerrank.com/challenges/recursive-digit-sum/problem'),
    'p2_05_insertionsort1': ('Insertion Sort - Part 1', 'https://www.hackerrank.com/challenges/insertionsort1/problem'),
    'p2_06_insertionsort2': ('Insertion Sort - Part 2', 'https://www.hackerrank.com/challenges/insertionsort2/problem')
}

if __name__ == '__main__':
    main()
