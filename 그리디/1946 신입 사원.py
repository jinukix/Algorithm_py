import sys
input = sys.stdin.readline

t = int(input())
ans = []

for i in range(t):
    n = int(input())

    data = [0 for i in range(n + 1)]

    for i in range(n):
        a, b = map(int, input().split())
        data[a] = b

    min_r = data[1]
    cnt = 1

    for i in range(2, n+1):
        if min_r > data[i]:
            min_r = data[i]
            cnt += 1

    ans.append(cnt)

for i in ans:
    print(i)
