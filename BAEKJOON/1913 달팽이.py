import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
m = int(read())

arr = [[0 for _ in range(n)] for _ in range(n)]

num = n*n
dir = 0  # 남 동 북 서
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
y, x = 0, 0

for i in range(n*n):
    if num == m:
        a, b = y+1, x+1

    arr[y][x] = num
    num -= 1

    ny = y + dy[dir]
    nx = x + dx[dir]

    if (ny < 0 or ny >= n) or (nx < 0 or nx >= n) or arr[ny][nx] != 0:
        dir = (dir + 1) % 4
        y = y + dy[dir]
        x = x + dx[dir]
    else:
        y = ny
        x = nx

for i in arr:
    for j in i:
        print(j, end=" ")
    print()

print(a, b)
