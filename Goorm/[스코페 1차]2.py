import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
road = read()
dp = [0 for i in range(n)]
dp[0] = 1

if road[1] == "1":
    dp[1] = 1

for i in range(2, n):
    if road[i] == "0":
        continue

    if road[i - 2] == "1":
        dp[i] += dp[i - 2]
    if road[i - 1] == "1":
        dp[i] += dp[i - 1]

print(dp[n - 1])


"""

경로를 직선화
1. 방문해야하는 곳 1 방문하지 말아야할 곳 0
2. 각 문자 사이 간격 1
3. 한 번에 한칸 or 두칸 이동

왼쪽끝 -> 오른쪽 끝 : 몇가지 경우의 수


"""