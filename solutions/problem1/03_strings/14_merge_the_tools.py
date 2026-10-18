def merge_the_tools(string, k):
    for start in range(0, len(string), k):
        chunk = string[start:start + k]
        # dict.fromkeys keeps the first occurrence of each char, in order
        print("".join(dict.fromkeys(chunk)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
