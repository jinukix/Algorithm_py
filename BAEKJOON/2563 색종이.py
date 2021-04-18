import sys


def read():
    return sys.stdin.readline().strip()


graph = [[0 for _ in range(101)] for _ in range(101)]
n = int(read())

for i in range(n):
    a, b = map(int, read().split())

    for y in range(a, a + 10):
        for x in range(b, b + 10):
            graph[y][x] = 1

cnt = 0
for row in graph:
    cnt += row.count(1)

print(cnt)
