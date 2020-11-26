n, k = map(int, input().split())
cnt = 0

l = []

for i in range(n):
    l.append(int(input()))

for i in range(n-1, -1, -1):
    if k >= l[i]:
        share = k//l[i]
        cnt += share
        k -= l[i] * share

    if k == 0:
        break

print(cnt)
