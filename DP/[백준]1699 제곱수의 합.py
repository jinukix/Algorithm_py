import sys

def read():
    return sys.stdin.readline().strip()


n = int(read())

dp = [0] + [0 for i in range(n)]

for i in range(1, n+1):
    dp[i] = i  # 처음에는 1으로만 만든다고 치고 i값 넣어주기.

    for j in range(1, i):
        if (j*j) > i:  # 제곱했을때 i보다 크면 거르기.
            break

        if dp[i] > dp[i - (j * j)] + 1:
            dp[i] = dp[i - (j * j)] + 1
        # dp[i] = min(dp[i], dp[i-(j*j)] + 1)
        # min으로 하면 시간초과가 뜬다.... if로 걸러주는게 더 빠르다..


print(dp[n])
