import heapq

n = int(input())
p = []
w = 0
maxW = 0


for i in range(n):
    heapq.heappush(p, int(input()))

roaf_cnt = len(p)

for i in range(roaf_cnt):
    s = heapq.heappop(p)
    w = s*roaf_cnt
    roaf_cnt -= 1

    if maxW < w:
        maxW = w

print(maxW)
