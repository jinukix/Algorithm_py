import sys

def read():
    return sys.stdin.readline().strip()

n = int(read())
coin = [500, 100, 50, 10, 5, 1]

cnt = 0
share = 0

m = 1000 - n

for i in coin:
    if m >= i:
        share = m//i
        m -= i * share
        cnt += share

print(cnt)
