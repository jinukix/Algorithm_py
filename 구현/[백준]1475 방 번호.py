import sys
import math


def read():
    return sys.stdin.readline()


n = read().rstrip()
num = [0 for i in range(9)]
cnt = 0

for i in range(len(n)):
    x = int(n[i])

    if x == 6 or x == 9:
        num[6] += 0.5
    else:
        num[x] += 1

num[6] = math.ceil(num[6])  # 올림
print(int(max(num)))
