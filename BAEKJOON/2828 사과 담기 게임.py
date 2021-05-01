import sys


def read():
    return sys.stdin.readline().strip()


n, m = map(int, read().split())
j = int(read())

start = 1
end = m
ans = 0

for i in range(j):
    x = int(read())

    if start > x:
        ans += start - x
        start = x
        end = x + m - 1

    elif end < x:
        ans += x - end
        end = x
        start = end - m + 1

print(ans)
