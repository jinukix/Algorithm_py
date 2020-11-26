# https://www.acmicpc.net/problem/10844

'''python
맨 뒤에 올수 있는 숫자를 기준으로 풀면된다.
dp[i][j] = i번째 자리에 j숫자가 마지막으로 오는 경우의 수
세가지 경우의 수가 있다.
1. j == 0
-> dp[i-1][1] i-1번째 자리가 1으로 끝나는 경우의 수
2. j == 9
-> dp[i-1][8]
3. j == 1~8 
-> dp[i-1][j-1] + dp[i-1][j+1] 

'''

import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    dp[0][i] = 1


for i in range(1, n):

    for j in range(10):

        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]


print(sum(dp[n-1]) % 1000000000)
