"""
# sticker[i][0] = i번째에 첫째 줄 스티커의 점수,
# sticker[i][1] = i번째에 둘째 줄 스티커의 점수이다.

# dp[i][0] = i번째 첫째 줄 스티커를 선택했을 때 최대 점수이다.
# 단 i번째 첫째 줄 스티커가 포함되지 않더라도 dp[i-1][0]값과 비교해 더 큰값을 넣어준다.
# -> dp[i][0] = max(dp[i-1][0], sticker[i][0] + dp[i-1][1])

# 둘째 줄도 마찬가지로 계산해주면 된다.
"""

import sys


def read():
    return sys.stdin.readline().strip()


t = int(read())

sticker = [[0, 0] for i in range(100001)]
dp = [[0, 0] for i in range(100001)]

for i in range(t):

    n = int(read())

    data0 = list(map(int, read().split()))
    for i in range(n):
        sticker[i][0] = data0[i]

    data1 = list(map(int, read().split()))
    for i in range(n):
        sticker[i][1] = data1[i]

    dp[0][0] = sticker[0][0]
    dp[0][1] = sticker[0][1]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], sticker[i][0] + dp[i-1][1])
        dp[i][1] = max(dp[i-1][1], sticker[i][1] + dp[i-1][0])

    print(max(dp[n-1]))