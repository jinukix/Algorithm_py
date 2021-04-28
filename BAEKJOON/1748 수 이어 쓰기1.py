import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())

ans = 0
ten = 1
l = 1

while ten <= n:
    x = ten * 10 - 1

    if x >= n:
        ans += (n - ten + 1) * l
    else:
        ans += (x - ten + 1) * l

    ten *= 10
    l += 1

print(ans)