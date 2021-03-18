import sys
import heapq


def read():
    return sys.stdin.readline().strip()


n = int(read())
q = []


for _ in range(n):
    heapq.heappush(q, int(read()))

ans = 0
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)

    ans += a+b
    heapq.heappush(q, a+b)


print(ans)
