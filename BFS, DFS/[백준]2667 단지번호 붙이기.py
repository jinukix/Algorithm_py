# DFS


import sys


def read():
    return sys.stdin.readline().strip()


def dfs(y, x):

    global cnt  # 함수 내에서 global로 전역변수 선언하기.
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if graph[y][x] == 1:
        graph[y][x] = 0
        cnt += 1
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)


n = int(read())

graph = [list(map(int, read())) for i in range(n)]

ans = []
cnt = 0

for i in range(n):
    for j in range(n):
        dfs(i, j)
        if cnt != 0:
            ans.append(cnt)
            cnt = 0

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
