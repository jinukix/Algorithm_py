import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(virus):
    q = deque(virus)

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    while q:
        virus_num, virus_y, virus_x, virus_t = q.popleft()

        if virus_t >= s:
            break

        for i in range(4):
            ny = virus_y + dy[i]
            nx = virus_x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 0:
                graph[ny][nx] = virus_num
                q.append([graph[ny][nx], ny, nx, virus_t+1])


n, k = map(int, read().split())

graph = [list(map(int, read().split()))for _ in range(n)]
s, x, y = map(int, read().split())

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append([graph[i][j], i, j, 0])

virus.sort()

bfs(virus)

print(graph[x-1][y-1])
