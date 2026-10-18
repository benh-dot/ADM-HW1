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
