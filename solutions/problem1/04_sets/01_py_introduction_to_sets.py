def average(array):
    distinct = set(array)
    return round(sum(distinct) / len(distinct), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
