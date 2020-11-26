import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(start):
    q = deque([start])

    while q:
        v = q.popleft()

        for i in graph[v]:
            if parent[i] == 0:
                parent[i] = v
                q.append(i)


n = int(read())
graph = [[] for i in range(n+1)]
parent = [0 for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)


bfs(1)

for i in range(2, n+1):
    print(parent[i])
