import sys


def read():
    return sys.stdin.readline().strip()


a, b = map(int, read().split())

arr = []
for i in range(1, 46):
    arr += [i] * i

ans = sum(arr[a-1:b])
print(ans)
