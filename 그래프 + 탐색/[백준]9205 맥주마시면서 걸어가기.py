import sys


def read():
    return sys.stdin.readline().strip()


INF = 1e9

t = int(read())

for _ in range(t):
    n = int(read())
    a = [list(map(int, read().split())) for i in range(n+2)]
    d = [[INF] * (n+2) for i in range(n+2)]

    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue

            if abs(a[i][0]-a[j][0]) + abs(a[i][1]-a[j][1]) <= 1000:
                d[i][j] = 1

    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    if d[0][n+1] < INF:
        print("happy")
    else:
        print("sad")
