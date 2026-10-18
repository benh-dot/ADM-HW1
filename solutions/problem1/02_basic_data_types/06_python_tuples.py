def tuple_hash(t):
    # HackerRank's expected output was produced with the classic tuple hash
    # (CPython <= 3.7 / PyPy). Newer CPython changed hash(tuple), so the
    # classic algorithm is reproduced here with 64-bit arithmetic: this gives
    # the expected answer in both Python 3 and PyPy 3.
    mask = (1 << 64) - 1
    x = 0x345678
    mult = 1000003
    remaining = len(t)
    for item in t:
        remaining -= 1
        x = ((x ^ (hash(item) & mask)) * mult) & mask
        mult = (mult + 82520 + remaining + remaining) & mask
    x = (x + 97531) & mask
    if x == mask:
        x = mask - 1
    return x - (1 << 64) if x >= (1 << 63) else x


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(tuple_hash(tuple(integer_list)))
