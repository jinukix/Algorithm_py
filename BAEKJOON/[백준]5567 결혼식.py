import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(start):
    q = deque([start])
    l = 2
    cnt = 0
    visited = [0 for i in range(n+1)]
    visited[start] = 1

    while q and l:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                if visited[i] > 3:
                    break
                cnt += 1
                q.append(i)

    return cnt


n = int(read())
m = int(read())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))
