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
