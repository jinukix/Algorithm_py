import sys

def read():
    return sys.stdin.readline().strip()


n = int(read())

l = list(map(int, input().split()))
price = list(map(int, input().split()))

pr = price[0]
ans = 0

for i in range(n-1):
    le = l[i]

    if pr > price[i]:
        pr = price[i]

    ans += le * pr

print(ans)
