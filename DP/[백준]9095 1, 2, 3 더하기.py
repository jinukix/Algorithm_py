'''
규칙을 찾아보면 쉽게 풀수있는 문제이다.
예시로 4라는 숫자를 만들때
1에서 +3 => dp[3] / 1+(1+1+1), 1+(1+2), 1+(2+2), 1+(3)
2에서 +2 => dp[2] / 1+1+(2), 2+(2)
3에서 +1 => dp[1] / 3+(1)
의 방법이 존재한다. (괄호 쳐놓은 숫자가 추가된 숫자이다.)
=> dp[n] = dp[n-1] + dp[n-2] + dp[n-3]이라는 것을 알 수 있다.
'''

import sys

def read():
    return sys.stdin.readline().strip()


t = int(read())

dp = [1, 2, 4]

for i in range(3, 10):  # n은 11보다 작다.
    dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

for i in range(t):
    n = int(read())
    print(dp[n - 1])
