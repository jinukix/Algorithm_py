'''
dp문제는 점화식을 찾는 것이 가장 중요하다.
두 가지 경우만 구해주면 된다.
1. 맨 오른쪽에 2x1 블럭을 한 개(1칸) 놓는 경우 dp[n-1] 
2. 맨 오른쪽에 1x2 블럭을 두 개(2칸) 놓는 경우 dp[n-2]
dp[n] = dp[n-1] + dp[n-2]인 것을 알 수 있다.
'''

import sys

def read():
    return sys.stdin.readline().strip()


block = [0, 1, 2]

n = int(input())

for i in range(3, n+1):
    block.append(block[i - 2] + block[i - 1])

print(block[n] % 10007)
