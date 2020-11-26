import sys
sys.setrecursionlimit(50000)  # 재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000


def read():
    return sys.stdin.readline().strip()


def dfs(y, x):

    graph[y][x] = 1
    global cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny >= 0 and ny < m and nx >= 0 and nx < n and graph[ny][nx] == 0:
            cnt += 1
            dfs(ny, nx)


m, n, k = map(int, read().split())

graph = [[0 for i in range(n)]for i in range(m)]

for i in range(k):
    a, b, c, d = map(int, read().split())

    for j in range(b, d):
        for k in range(a, c):
            graph[j][k] = 1


ans = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            cnt = 1
            dfs(y, x)
            ans.append(cnt)


print(len(ans))
ans.sort()

for i in ans:
    print(i, end=" ")
