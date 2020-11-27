import sys
sys.setrecursionlimit(50000)  # 재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000


def read():
    return sys.stdin.readline().strip()


def dfs(y, x):
    graph[y][x] = 0

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if (ny >= 0 and ny < n) and (nx >= 0 and nx < m):
            if graph[ny][nx] == 1:
                dfs(ny, nx)


time = int(read())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for t in range(time):
    m, n, k = map(int, read().split())
    graph = [[0 for i in range(m)] for i in range(n)]

    for i in range(k):
        a, b = map(int, read().split())
        graph[b][a] = 1

    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                dfs(y, x)
                cnt += 1

    print(cnt)
