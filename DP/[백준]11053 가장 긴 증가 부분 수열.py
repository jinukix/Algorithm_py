# https://www.acmicpc.net/problem/11053

'''python
dp에 각각 수열의 길이를 넣어준다.
자기 자신보다 작은 숫자를 찾고 가장 큰 길이의 +1 값을 넣어주면 된다.

'''

import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())

num = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if num[i] > num[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
