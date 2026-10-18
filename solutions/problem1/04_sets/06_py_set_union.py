input()
english = set(input().split())
input()
french = set(input().split())

print(len(english.union(french)))
