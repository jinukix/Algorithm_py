'''
dp를 2차원 배열로 두가지 값을 저장해서 풀었다.
dp[i][0] = i번째 까지의 값을 더한 값. 음수가 됬다면 0으로 초기화.
dp[i][1] = i번째 까지의 최댓값
해당 점화식을 구하고 문제를 제출했으나 오답처리가 됬다.
점화식에 대한 오류를 찾아봤는데 반례를 찾지못한체 
삽질을 거듭한 끝에 모든 수가 음수였을때 발생하는 오류라는 것을 발견했다.
해당 반례를 처리해주고 끝.
문제를 풀다보니 이런 사소한 실수를 놓치는 경우가 많은것 같다.
이번 경우에도 점화식을 구하는것은 쉬웠으나
저 실수 때문에 시간이 배 이상이 걸렸다.
반성
'''

import sys

def read():
    return sys.stdin.readline().strip()


n = int(read())

num = list(map(int, read().split()))
dp = [[0, 0] for i in range(n)]

dp[0][0] = num[0]
dp[0][1] = num[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + num[i], 0)  # 마지막 수를 포함. 음수라면 0으로
    dp[i][1] = max(dp[i-1][1], dp[i][0])  # 최대수

maxnum = max(num)

if maxnum < 0:
    print(maxnum)
else:
    print(dp[n-1][1])
