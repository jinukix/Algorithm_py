import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(start):

    q = deque([start])

    while q:
        v = q.popleft()
        for i in graph[v]:
            if num[start][i] == 0:
                q.append(i)
                num[start][i] = num[start][v] + 1

    return sum(num[start])


n, m = map(int, read().split())

graph = [[] for i in range(n+1)]
num = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

min_sum = 1e9
idx = 0

for i in range(1, n+1):
    if min_sum > bfs(i):
        min_sum = bfs(i)
        idx = i

print(idx)
