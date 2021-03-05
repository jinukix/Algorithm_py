import sys

def read():
    return sys.stdin.readline().strip()


t = int(input())

data = [300, 60, 10]
ans = [0 for i in range(3)]

for i in range(len(data)):
    if t >= data[i]:
        share = t//data[i]
        t -= data[i] * share
        ans[i] += share

if t == 0:
    for i in range(len(ans)):
        print(ans[i], end=" ")
else:
    print(-1)
