def solution(land):
    l = len(land)
    dp = [[0 for i in range(4)] for i in range(l)]

    for i in range(len(land[0])):
        dp[0][i] = land[0][i]

    for i in range(1, l):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][j-1], dp[i-1][j-2], dp[i-1][j-3])

    return max(dp[l-1])