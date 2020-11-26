import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, input().strip())) for i in range(n)]
b = [list(map(int, input().strip())) for i in range(n)]

cnt = 0


def change(i, j):
    for y in range(3):
        for x in range(3):
            a[i+y][j+x] = 1 - a[i+y][j+x]


for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            change(i, j)
            cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)
