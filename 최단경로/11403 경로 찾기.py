import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())

graph = [list(map(int, read().split())) for i in range(n)]

for k in range(n):  # 경로가 가장 상단 이여야 한다
    for i in range(n):
        for j in range(n):
            if (graph[i][k] and graph[k][j]) or graph[i][j]:
                graph[i][j] = 1


# 출력
for i in graph:
    for j in i:
        print(j, end=" ")
    print()
