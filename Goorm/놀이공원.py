import sys


def read():
    return sys.stdin.readline()


def check(y, x, k):
    cnt = 0
    for i in range(y, y + k):
        for j in range(x, x + k):
            if maps[i][j] == 1:
                cnt += 1
    return cnt


t = int(read())

for _ in range(t):
    n, k = map(int, read().split())

    maps = [list(map(int, read().split())) for _ in range(n)]
    ans = n * n

    r = n - k + 1

    for y in range(r):
        for x in range(r):
            cnt = check(y, x, k)
            if ans > cnt:
                ans = cnt

    print(ans)