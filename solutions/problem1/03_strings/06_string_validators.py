if __name__ == '__main__':
    s = input()
    for check in (str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper):
        print(any(check(c) for c in s))
