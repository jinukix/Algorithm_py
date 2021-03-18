import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(y, x):

    ans = [[[0, 0] for i in range(m)]for i in range(n)]
    ans[y][x][0] = 1
    q = deque([[y, x, 0]])

    while q:

        y, x, b = q.popleft()

        if y == n-1 and x == m-1:
            print(ans[y][x][b])
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:

                if graph[ny][nx] == 1 and b == 0:
                    q.append([ny, nx, 1])
                    ans[ny][nx][1] = ans[y][x][b]+1

                elif graph[ny][nx] == 0 and ans[ny][nx][b] == 0:
                    q.append([ny, nx, b])
                    ans[ny][nx][b] = ans[y][x][b]+1

    print(-1)


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

n, m = map(int, read().split())
graph = [list(map(int, read())) for i in range(n)]

bfs(0, 0)
