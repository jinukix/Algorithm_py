import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(start):
    q = deque([[start, 0]])
    visited[start] = True

    while q:
        v, t = q.popleft()
        if t == k:
            ans.append(v)
        elif t < k:
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = True
                    q.append([i, t+1])


n, m, k, x = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)

ans = []

bfs(x)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
