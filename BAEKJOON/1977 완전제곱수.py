import sys


def read():
    return sys.stdin.readline()


m = int(read())
n = int(read())

ans = []

for i in range(101):
    num = i * i

    if m <= num and num <= n:
        ans.append(num)
    elif num > m:
        break

if len(ans) == 0:
    print("-1")
else:
    print(sum(ans))
    print(ans[0])
