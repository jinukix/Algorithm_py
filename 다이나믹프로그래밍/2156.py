# https://www.acmicpc.net/problem/2156

'''python

세가지의 경우가 있다.
마지막 와인의 번호를 i라고 할때
1.i, i-1와인을 포함하고 i-3까지의 dp값.
2.i와인을 포함하고 i-2까지의 dp값
3.i-1까지의 dp값
이 세가지 경우의 값에서 가장 큰 값을 대입해주면된다.

'''

import sys


def read():
    return sys.stdin.readline().strip()


n = int(input())
wine = [0 for i in range(n)]
dp = [0 for i in range(n)]

for i in range(n):
    wine[i] = int(read())


for i in range(n):
    if i == 0:
        dp[0] = wine[0]
    elif i == 1:
        dp[1] = dp[0] + wine[1]
    elif i == 2:
        dp[2] = max(dp[1], wine[2] + wine[0], wine[2] + wine[1])
    else:
        a = wine[i] + wine[i-1] + dp[i-3]
        b = wine[i] + dp[i-2]
        c = dp[i-1]
        dp[i] = max(a, b, c)


print(dp[n-1])
