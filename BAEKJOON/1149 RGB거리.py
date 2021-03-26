"""
n번째 집을 R로 칠할 때 최소 비용 = min(n-1번째 집을 G로 칠할 때 최소 비용,n-1번째 집을 B로 칠할 때 최소 비용)
n번째 집을 G로 칠할 때 최소 비용 = min(n-1번째 집을 R로 칠할 때 최소 비용,n-1번째 집을 B로 칠할 때 최소 비용)
n번째 집을 B로 칠할 때 최소 비용 = min(n-1번째 집을 R로 칠할 때 최소 비용,n-1번째 집을 G로 칠할 때 최소 비용)
3가지 경우에서 최소 비용을 찾아 출력해주면 된다.
"""

import sys


def read():
    return sys.stdin.readline().strip()


n = int(input())

color = []
for i in range(n):
    color.append(list(map(int, read().split())))


dp = []
for i in range(n):
    if i == 0:
        a = color[i][0]
        b = color[i][1]
        c = color[i][2]
        dp.append([a, b, c])
    else:
        a = color[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        b = color[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        c = color[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        dp.append([a, b, c])


ans = min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])

print(ans)
