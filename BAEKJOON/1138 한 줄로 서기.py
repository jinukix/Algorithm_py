import sys

def read():
    return sys.stdin.readline()

n = int(read())
data = list(map(int, read().split()))

p = [0 for _ in range(n)]

for i in range(n):
    cnt = 0 
    for j in range(n):
        if cnt == data[i] and not p[j]:
            p[j] = i+1
            break
        elif not p[j]:
            cnt += 1

for i in range(n):
    print(p[i], end=" ")
