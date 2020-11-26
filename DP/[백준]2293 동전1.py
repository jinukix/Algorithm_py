# https://www.acmicpc.net/problem/2293

'''python
dp[k]는 k원을 만들 수 있는 경우의 수이다.
동전을 하나씩 사용해 동전의 종류를 늘려가며 해당 동전으로 만들 수 있는 경우의 수를 찾아 더해가면 된다.
동전의 금액부터 ~ k원까지 탐색을 해 탐색중인 금액을 j라고 할 때
dp[j]에서 dp[j-(동전의 금액)]을 더해주면 된다.

'''


import sys


def read():
    return sys.stdin.readline().strip()


n, k = map(int, read().split())

coin = [int(read()) for i in range(n)]
dp = [0 for i in range(10001)]

dp[0] = 1

for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])
