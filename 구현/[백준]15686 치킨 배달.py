import sys
from itertools import combinations


def read():
    return sys.stdin.readline()


n, m = map(int, read().split())

map = [list(map(int, read().split()))for _ in range(n)]

ch = []
home = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 2:
            ch.append([i, j])
        elif map[i][j] == 1:
            home.append([i, j])


ch = list(combinations(ch, m))

ans = []

for i in range(len(ch)):

    sum = 0
    for j in range(len(home)):

        min_l = 0

        for k in range(m):
            l = abs(ch[i][k][0] - home[j][0]) + abs(ch[i][k][1] - home[j][1])

            if min_l > l or min_l == 0:
                min_l = l

        sum += min_l
    ans.append(sum)

print(min(ans))
