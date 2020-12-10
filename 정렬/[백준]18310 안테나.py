import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())

data = list(map(int, read().split()))
data.sort()

print(data[(n-1)//2])
