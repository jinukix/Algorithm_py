import sys
sys.setrecursionlimit(50000)  # 재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000


def read():
    return sys.stdin.readline().strip()


def dfs(y, x, color):
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:

            if check:
                if color == graph[ny][nx]:
                    dfs(ny, nx, color)
            else:
                if color == 'B':
                    if graph[ny][nx] == 'B':
                        dfs(ny, nx, color)
                else:
                    if graph[ny][nx] == 'G' or graph[ny][nx] == 'R':
                        dfs(ny, nx, color)


n = int(read())
graph = [read() for i in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

visited = [[False for i in range(n)] for i in range(n)]
cnt = 0
check = True

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(y, x, graph[y][x])
            cnt += 1

visited = [[False for i in range(n)] for i in range(n)]
cntt = 0
check = False

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(y, x, graph[y][x])
            cntt += 1


print(cnt, cntt)
