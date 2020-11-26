import sys


# http://melonicedlatte.com/algorithm/2018/03/15/181550.html
# 문제가 너무어렵다 위에거 참고해서 풀었음.

def read():
    return sys.stdin.readline().strip()


str1 = read()
str2 = read()

len1 = len(str1)
len2 = len(str2)

# dp[i][j] = i번째 문자와 j번째 문자 사이의 LCS길이
dp = [[0 for i in range(len2 + 1)] for i in range(len1 + 1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1],
                       (dp[i-1][j-1]+(str1[i-1] == str2[j-1])))

print(dp[len1][len2])
