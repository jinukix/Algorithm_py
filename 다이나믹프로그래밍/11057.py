# https://www.acmicpc.net/problem/11057

'''python
간단한 문제이다.
dp[i][j]를 i길이의 j숫자가 마지막으로 오는 경우의 수라고 생각하고 풀면된다.
i-1길이의 경우에서 j보다 같거나 작은 숫자가f 오는 경우를 더해주면된다.(k <= j)
dp[i][j] += dp[i-1][k]의 점화식이 성립하게 된다.
'''


import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())

dp = [[0 for _ in range(10)] for _ in range(n)]

for i in range(10):
    dp[0][i] = i+1

for i in range(1, n):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(max(dp[n-1]) % 10007)
