import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(y, x):
    queue = deque([(y, x)])
    graph[y][x] = 1
    cnt = 1

    while queue:  # 큐가 빌 때까지.

        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= 0 and ny < n and nx >= 0 and nx < m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((ny, nx))


n, m = map(int, read().split())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

graph = [list(map(int, read())) for i in range(n)]

bfs(0, 0)

print(graph[n-1][m-1])
