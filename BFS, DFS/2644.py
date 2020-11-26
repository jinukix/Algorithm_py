import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(start):
    q = deque([start])

    while q:
        v = q.popleft()
        for i in graph[v]:
            if i == end:
                return rel[v]+1
            if rel[i] == 0:
                q.append(i)
                rel[i] = rel[v]+1
    return -1


n = int(read())
start, end = map(int, read().split())
m = int(read())

graph = [[] for i in range(n+1)]
rel = [0 for i in range(n+1)]

for i in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

if start == end:
    print(0)
else:
    print(bfs(start))
