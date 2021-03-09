def solution(n):
    
    dp = [0 for i in range(n)]

    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return (dp[n-1] + dp[n-2]) % 1234567