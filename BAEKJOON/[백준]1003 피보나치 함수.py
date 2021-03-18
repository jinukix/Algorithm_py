# https://www.acmicpc.net/problem/1003

'''
규칙을 알아내면 단순한 문제이다.
dp[0] = [1,0] 0이 1개, 1이 0개
dp[1] = [0,1] 0이 0개, 1이 1개
->
dp[2][0] = dp[0][0] + dp[1][0]
dp[2][1] = dp[1][1] + dp[0][1]
dp[2] = [1,1]이 되는 것을 알 수 있다.
->
즉 dp[n] = [dp[n-2][0] + dp[n-1][0], dp[n-2][1] + dp[n-1][1]]이다.

'''

import sys


def read():
    return sys.stdin.readline().strip()


dp = [[1, 0], [0, 1]]

for i in range(2, 41):
    a = dp[i-2][0] + dp[i-1][0]
    b = dp[i-2][1] + dp[i-1][1]
    dp.append([a, b])

t = int(read())
ans = []

for i in range(t):
    n = int(read())
    ans.append(dp[n])

for i in range(t):
    print(f"{ans[i][0]} {ans[i][1]}")
