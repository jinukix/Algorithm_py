import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(array):

    queue = deque(array)

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= 0 and ny < n and nx >= 0 and nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny, nx])


m, n = map(int, read().split())

graph = [list(map(int, read().split())) for i in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

array = []
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            array.append([y, x])

bfs(array)

max_num = 0
have0 = False

for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            have0 = True
            break
        else:
            if graph[y][x] > max_num:
                max_num = graph[y][x]


if have0:
    print(-1)
else:
    print(max_num-1)
