import sys
sys.setrecursionlimit(50000)  # 재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000


def read():
    return sys.stdin.readline().strip()


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, read().split())

graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]


for i in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)


cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
