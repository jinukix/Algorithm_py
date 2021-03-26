import sys
import heapq


def read():
    return sys.stdin.readline().strip()


n, k = map(int, read().split())
dia = []
check = []

for _ in range(n):
    a = list(map(int, read().split()))
    dia.append(a)

for _ in range(k):
    check.append(int(read()))

dia.sort()
check.sort()

max_heap = []
cnt = 0
result = 0

for i in range(k):
    while cnt < n and check[i] >= dia[cnt][0]:
        heapq.heappush(max_heap, -dia[cnt][1])
        cnt += 1

    if len(max_heap) > 0:
        max_num = heapq.heappop(max_heap)
        result += abs(max_num)

print(result)
