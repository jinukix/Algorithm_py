import sys


def read():
    return sys.stdin.readline()


t = int(read())

for _ in range(t):
    n, m = map(int, read().split())
    data = list(map(int, read().split()))

    idx = m
    cnt = 0

    while True:
        if data[0] != max(data):
            data.append(data.pop(0))
            if idx == 0:
                idx = len(data) - 1
            else:
                idx -= 1
        else:
            cnt += 1
            if idx == 0:
                print(cnt)
                break
            data.pop(0)
            idx -= 1
