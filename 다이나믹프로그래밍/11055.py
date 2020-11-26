import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
num = list(map(int, read().split()))
dp = [0 for i in range(n+1)]

for i in range(n):
    dp[i] = num[i]
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+num[i])

print(max(dp))
