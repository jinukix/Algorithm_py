# https://www.acmicpc.net/problem/11052

'''python
dp[i] 를 i를 만드는 금액의 최댓값으로 생각한다.
i를 만드는 방법은
1. card[i]를 1개 사용.
2. dp[i-j] + dp[j]이다.
*배열의 특성상 0부터 시작되므로 i-j에 -1을 해주자. 
만약 -1을 해주지 않는다면 dp[2] = dp[2-0] + dp[0]과 같은 경우가 나올 수 있다.

'''

import sys


def read():
    return sys.stdin.readline()


n = int(read())
card = list(map(int, read().split()))
dp = [0 for i in range(n)]

dp[0] = card[0]
dp[1] = max(card[1], card[0]*2)

for i in range(2, n):
    dp[i] = card[i]
    for j in range((i//2)+1):
        dp[i] = max(dp[i], dp[i-j-1]+dp[j])


print(dp[n-1])
