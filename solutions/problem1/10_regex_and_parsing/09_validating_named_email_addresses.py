import re
import email.utils

# username: starts with a letter, then letters/digits/-/./_ ; domain: letters ;
# extension: 1-3 letters
pattern = re.compile(r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

for _ in range(int(input())):
    line = input().strip()
    name, addr = email.utils.parseaddr(line)
    if pattern.match(addr):
        print(line)
