import sys


def read():
    return sys.stdin.readline()


n, k = map(int, read().split())

data = [i for i in range(2, n+1)]

ans = 0

while k > 0:
    m = min(data)
    for i in data:
        if i % m == 0:
            if k == 1:
                print(i)
            data.remove(i)
            k -= 1
