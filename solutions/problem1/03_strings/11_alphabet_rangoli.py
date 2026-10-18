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
