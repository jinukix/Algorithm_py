import sys
from collections import deque


def read():
    return sys.stdin.readline().strip()


def bfs(n, k):
    queue = deque([n])

    while queue:
        v = queue.popleft()

        if v == k:
            return time[v]

        for i in (v-1, v+1, v*2):
            if 0 <= i and i < MAX and time[i] == 0:
                time[i] = time[v] + 1
                queue.append(i)


MAX = 100001
n, k = map(int, read().split())
time = [0 for i in range(MAX)]
print(bfs(n, k))
