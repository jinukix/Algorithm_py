import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(start):

    q = deque([start])

    while q:
        y, x = q.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny == goal[0] and nx == goal[1]:
                return graph[y][x] + 1

            if 0 <= ny < l and 0 <= nx < l and graph[ny][nx] == 0:
                q.append([ny, nx])
                graph[ny][nx] = graph[y][x] + 1


t = int(read())
dy = [1, -1, 2, -2, 2, -2, 1, -1]
dx = [-2, -2, -1, -1, 1, 1, 2, 2]

for _ in range(t):
    l = int(read())
    graph = [[0 for i in range(l)]for i in range(l)]

    start = list(map(int, read().split()))
    goal = list(map(int, read().split()))

    if start == goal:
        print(0)
    else:
        print(bfs(start))
