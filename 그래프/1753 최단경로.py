import sys
import heapq


def read():
    return sys.stdin.readline().strip()


def djk(start):
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if d[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = 1e9
v, e = map(int, read().split())
k = int(read())

graph = [[] for i in range(v+1)]
d = [INF for i in range(v+1)]

for i in range(e):
    a, b, c = map(int, read().split())
    graph[a].append([b, c])

djk(k)

for i in range(1, v+1):
    if d[i] == INF:
        print("INF")
    else:
        print(d[i])
