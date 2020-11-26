import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())

dp = [0 for i in range(n+1)]
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746  # 연산마다 나머지처리를 해줘야지 시간초과가 안뜬다.

print(dp[n-1])
