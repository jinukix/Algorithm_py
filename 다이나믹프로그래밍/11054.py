import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
num = list(map(int, read().split()))
dp = [[0, 0] for i in range(n+1)]


for i in range(n):
    dp[i][0] = 1  # 오름차순

    for j in range(i):
        if num[j] < num[i]:  # / 오름차순
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)


for i in range(n-1, -1, -1):
    dp[i][1] = 1  # 내림차순

    for j in range(i, n):
        if num[i] > num[j]:  # \ 내림차순
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

ans = [0 for i in range(n+1)]
for i in range(n):
    ans[i] = dp[i][0] + dp[i][1] - 1

print(max(ans))
