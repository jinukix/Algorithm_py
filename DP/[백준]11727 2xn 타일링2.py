'''
11726 2 x 타일링 문제와 비슷한 문제이다.
문제풀이도 거의 동일하다.

세 가지 경우만 구해주면 된다.
1. 맨 오른쪽에 2x1 블럭을 한 개(1칸) 놓는 경우 dp[n-1] 
2. 맨 오른쪽에 1x2 블럭을 두 개(2칸) 놓는 경우 dp[n-2]
3. 맨 오른쪽에 2x2 블럭을 한 개(2칸) 놓는 경우 dp[n-2]

dp[n] = dp[n-1] + dp[n-2] + dp[n-2]인 것을 알 수 있다.
'''
import sys

def read():
    return sys.stdin.readline().strip()


n = int(read())

dp = [1, 3, 5]

for i in range(3, n+1):
    dp.append(dp[i-2]+dp[i - 2] + dp[i - 1])

print(dp[n-1] % 10007)
