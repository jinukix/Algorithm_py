'''
마지막 도착 계단은 반드시 밟아야한다. 그렇다면 두가지의 경우가 있다.
마지막 계단을 n번째 라고 했을때
1. n-1번째 계단을 밟은 경우
n-2번째 계단은 밟지못한다. 
=> stair[n] + stair[n-1] + dp[n-3]
2. n-1번째 계단을 밟지 않은 경우.
n-2번째 계단은 반드시 밟아야한다.
=> stair[n] + dp[n-2]
두 값을 비교해 큰 값을 넣어주면 된다.
'''

import sys

def read():
    return sys.stdin.readline().strip()


n = int(input())

stair = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    stair[i] = int(input())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = stair[2] + max(stair[0], stair[1])

for i in range(3, n):
    dp[i] = stair[i] + max((stair[i-1]+dp[i-3]), dp[i-2])

print(dp[n-1])
