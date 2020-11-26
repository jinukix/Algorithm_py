import sys


def read():
    return sys.stdin.readline()


n = int(read())

data = list(map(int, read().split()))
dp = [0] * n

dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if data[i] == data[j] + 1:
            dp[i] = dp[j]
            break
    dp[i] += 1

print(n-max(dp))
