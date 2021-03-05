import sys
import heapq

def read():
    return sys.stdin.readline().strip()


n, m = map(int, read().split())

data = list(map(int, read().split()))

heapq.heapify(data)  # heapq로 만들어주는 함수.

for i in range(m):
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    heapq.heappush(data, a+b)
    heapq.heappush(data, a+b)


print(sum(data))
