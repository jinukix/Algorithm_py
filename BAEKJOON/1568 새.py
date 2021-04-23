import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
k = 1
ans = 0

while n > 0:
    if n < k:
        k = 1
    n -= k
    k += 1
    ans += 1

print(ans)
