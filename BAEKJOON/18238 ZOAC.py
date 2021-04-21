import sys


def read():
    return sys.stdin.readline().strip()


chars = read()
start = "A"
ans = 0

for char in chars:
    ans += min(26 - abs(ord(start) - ord(char)), abs(ord(char) - ord(start)))
    start = char


print(ans)
