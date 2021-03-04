import sys

def read():
    return sys.stdin.readline()

n, l = map(int, read().split())
data = list(map(int, read().split()))
data.sort()

start = data[0]
end = data[0] + l
cnt = 1

for i in range(len(data)):
    if start <= data[i] < end:
        continue
    else:
        start = data[i]
        end = data[i] + l
        cnt += 1

print(cnt)
