import sys


def read():
    return sys.stdin.readline()


n = int(read())
k = int(read())

if k >= n:
    print(0)
else:
    data = list(map(int, read().split()))

    data.sort()

    dist = []

    for i in range(len(data)-1):
        dist.append(data[i+1] - data[i])

    dist.sort(reverse=True)

    for i in range(k-1):
        dist[i] = 0

    print(sum(dist))
