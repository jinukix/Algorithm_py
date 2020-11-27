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

        for i in grpah[now]:
            cost = i[1] + dist

            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = 1e9
n = int(read())
m = int(read())

grpah = [[] for i in range(n+1)]
d = [INF for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, read().split())
    grpah[a].append([b, c])

s, e = map(int, read().split())
djk(s)

print(d[e])
