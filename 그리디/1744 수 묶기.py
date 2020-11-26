import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for i in range(n)]

plus = []
minus = []

ans = 0

for i in data:
    if i <= 0:
        minus.append(i)
    elif i == 1:
        ans += 1
    elif i > 1:
        plus.append(i)

minus.sort()
plus.sort(reverse=True)

for i in range(0, len(minus), 2):
    if i+1 < len(minus):
        ans += minus[i] * minus[i+1]
    else:
        ans += minus[i]

for i in range(0, len(plus), 2):
    if i+1 < len(plus):
        ans += plus[i]*plus[i+1]
    else:
        ans += plus[i]

print(ans)
