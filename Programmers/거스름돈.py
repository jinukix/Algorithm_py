def solution(n, money):
    dp = [0 for i in range(n+1)]
    dp[0] = 1

    for i in money:
        for j in range(i, n+1):
            if j >= i:
                dp[j] += dp[j-i]
    
    ans = dp[n] % 1000000007
    return ans