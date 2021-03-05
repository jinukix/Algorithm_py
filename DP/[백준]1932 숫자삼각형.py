'''
dp배열을 2차원 배열로 만드는것이 포인트이다.
dp[i][j]가 i번째 층에서 j번째 원소를 포함한 경우의 합이라고 할 떄
1.현재층에서 첫번째 원소를 포함한 경우
-> dp[i-1][0]을 더해주면 된다.(현재 바로 윗층 첫번째 원소)
2.현재층에서 마지막 원소를 포함한 경우
-> dp[i-1][j-1]을 더해주면 된다.(현재 바로 윗층 마지막 원소)
3.현재층에서 중간에있는 원소를 포함한 경우.
-> dp[i-1][j-1]과 dp[i][j]값 중 더 큰값을 더해주면 된다.
'''

import sys

def read():
    return sys.stdin.readline().strip()


n = int(input())
dp = []

tri = []

for i in range(n):
    tri.append(list(map(int, read().split())))

for i in range(1, n+1):
    dp.append([0 for x in range(i)])

dp[0] = tri[0]

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = tri[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = tri[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = tri[i][j] + max(dp[i-1][j-1], dp[i-1][j])


print(max(dp[i]))
