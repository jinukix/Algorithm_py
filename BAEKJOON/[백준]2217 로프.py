import sys

def read():
    return sys.stdin.readline()

import heapq

n = int(read())
q = []
w = 0
maxW = 0

for i in range(n):
    heapq.heappush(q, int(read()))

roaf_cnt = len(q)

for i in range(roaf_cnt):
    s = heapq.heappop(q)
    w = s*roaf_cnt
    roaf_cnt -= 1

    if maxW < w:
        maxW = w

print(maxW)
