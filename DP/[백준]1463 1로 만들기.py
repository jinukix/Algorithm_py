# https://www.acmicpc.net/problem/1463

'''python
1. dp[n] 은 dp[n-1]+1을 넣어준다. # 1을 빼는 경우.
2. dp[n]이 2로 나누어떨어진다면, 1의 값과 dp[n//2]+1의 값을 비교해 작은 값을 넣는다.
3. dp[n]이 3로 나누어떨어진다면, 1의 값과 dp[n//3]+1의 값을 비교해 작은 값을 넣는다.
'''

import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
dp = [0 for i in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1]+1

    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2]+1

    if i % 3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3]+1


print(dp[n])
