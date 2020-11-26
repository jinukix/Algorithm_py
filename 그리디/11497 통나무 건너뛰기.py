import sys


def read():
    return sys.stdin.readline().strip()


test = int(read())

for t in range(test):
    n = int(read())

    data = list(map(int, read().split()))
    data.sort()

    p = []

    for i in range(0, n, 2):
        p.append(data[i])

    if n % 2 == 0:
        p.append(data[n-1])
        for i in range(n-3, 0, -2):
            p.append(data[i])
    else:
        for i in range(n-2, 0, -2):
            p.append(data[i])

    max = abs(p[0] - p[n-1])

    for i in range(n-1):
        lv = abs(p[i+1] - p[i])
        if max < lv:
            max = lv

    print(max)
