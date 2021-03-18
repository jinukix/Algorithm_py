
import sys
sys.setrecursionlimit(50000)  # 재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000


def read():
    return sys.stdin.readline().strip()


def dfs(y, x):
    graph[y][x] = 0

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue

        if graph[ny][nx] == 1:
            dfs(ny, nx)


dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [1, 0, -1, 1, -1, 1, 0, -1]

while True:
    w, h = map(int, read().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, read().split())) for i in range(h)]

    cnt = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                dfs(y, x)
                cnt += 1

    print(cnt)
