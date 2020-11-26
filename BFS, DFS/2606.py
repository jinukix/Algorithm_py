import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    global cnt

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1


n = int(read())
m = int(read())


graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

bfs(1, visited)
print(cnt)
