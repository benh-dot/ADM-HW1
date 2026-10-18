if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # distinct scores, sorted: the runner-up is the second largest
    print(sorted(set(arr))[-2])
