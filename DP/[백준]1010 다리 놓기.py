'''
dp[i][j] i개의 사이트에서 m개의 사이트를 잇는 경우의 수이다.
서쪽 사이트에서 다리 1개를 잇고 나머지 (n-1)개를 잇는 방법으로 풀었다.
dp[i][j] = dp[i-1][k] + dp[i-1][k-1].....
여기서 k는 j보다 작으면서 i-1보다 같거나 큰 값이여야 한다.
처음에 먼저 i가 0일때 dp[0][m] = m을 입력해주고
dp차례대로 값을 입력해 나가면 쉽게 풀 수 있는 문제이다.
'''

import sys

def read():
    return sys.stdin.readline().strip()


t = int(read())

for time in range(t):
    n, m = map(int, read().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        dp[0][i] = i+1

    for i in range(1, n):
        for j in range(i, m):
            for k in range(j-1, i-2, -1):
                dp[i][j] += dp[i-1][k]

    print(dp[n-1][m-1])
