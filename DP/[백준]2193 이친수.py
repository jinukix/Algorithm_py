'''
이친수들의 규칙을보면 10으로 시작한다는 것을 알 수 있다.
10ㅁㅁㅁㅁ...
10이후의 패턴만 찾아주면 쉽게 풀수있다.
라고 생각했는데 런타임 오류가 떠서 당황했다.
수많은 삽질 끝에 알고보니 n이 1의 경우일때 발생한 문제였고
for문을 돌려주기전에 dp[1] = 1이라고 써놓은것 때문이였다.T.T
'''

import sys

def read():
    return sys.stdin.readline().strip()


n = int(input())
dp = [0 for i in range(n)]
dp[0] = 1

for i in range(1, n):
    if i == 1:
        dp[1] = 1
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n-1])
