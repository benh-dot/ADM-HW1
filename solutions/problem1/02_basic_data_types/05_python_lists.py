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
