import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

p = [0 for i in range(n)]

key = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == data[i] and p[j] == 0:
            p[j] = key
            key += 1
            break
        elif p[j] == 0:
            cnt += 1

for i in range(n):
    print(p[i], end=" ")
