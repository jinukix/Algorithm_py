# https://www.acmicpc.net/problem/9461

# 파도반 수열

'''python

1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16.....
패턴이 보인다.
이전 삼각형 변의 길이와 n-5번째 삼각형 변의 길이를 더한 값이 된다.
점화식은 dp[n] = dp[n-1] + dp[n-5]

'''

import sys


def read():
    return sys.stdin.readline().strip()


dp = [1, 1, 1, 2, 2]

for i in range(5, 101):
    dp.append(dp[i-1] + dp[i-5])

t = int(read())

for i in range(t):
    n = int(read())
    print(dp[n-1])
