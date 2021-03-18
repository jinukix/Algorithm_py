# pypy3으로 제출

from collections import deque
import sys


def read():
    return sys.stdin.readline().strip()


def bfs(start):
    q = deque([start])
    cnt = 1
    visited = [False for i in range(n+1)]
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt


n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[b].append(a)

max_cnt = 0
ans = []
for i in range(1, n+1):
    if graph[i]:
        cnt = bfs(i)
        if max_cnt <= cnt:
            if max_cnt < cnt:
                ans = []
            max_cnt = cnt
            ans.append(i)

print(*ans)
