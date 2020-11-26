    # 
    

'''python
dp[i]는 i번째 상담을 마지막 포함해서 얻는 최대 수익이다.
첫번째로 i번째 상담이 마지막 날짜까지 기간이 가능한 상담이라면
dp[i]에 i번째 상담 수익을 넣는다.
마지막상담이 정해졌다면 처음부터 마지막 상담이전에 얻을 수 있는 경우를 비교해 주면 된다.
j번째 상담이 가능하다고 할때.
-> dp[i] = max(dp[i], dp[j] + meeting[i][1])
'''

import sys


def read():
    return sys.stdin.readline()


n = int(read())

meeting = [list(map(int, read().split())) for i in range(n)]
dp = [0 for i in range(n)]

for i in range(n):
    if i + meeting[i][0] <= n:
        dp[i] = meeting[i][1]
        for j in range(i):
            if j + meeting[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + meeting[i][1])

print(max(dp))
