import sys
import copy
from collections import deque
sys.setrecursionlimit(50000)


def read():
    return sys.stdin.readline().strip()


def bfs():
    global ans

    copy_graph = copy.deepcopy(graph)

    cnt = 0
    q = deque()

    for y in range(n):
        for x in range(m):
            if copy_graph[y][x] == 2:
                q.append([y, x])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if copy_graph[ny][nx] == 0:
                    copy_graph[ny][nx] = 2
                    q.append([ny, nx])

    for y in range(n):
        for x in range(m):
            if copy_graph[y][x] == 0:
                cnt += 1

    ans = max(ans, cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                graph[y][x] = 1
                wall(cnt+1)
                graph[y][x] = 0


n, m = map(int, read().split())

graph = [list(map(int, read().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0
wall(0)
print(ans)
