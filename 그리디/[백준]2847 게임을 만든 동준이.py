import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())  # lv

score = [int(read()) for i in range(n)]
cnt = 0

for i in range(n-1, 0, -1):
    if score[i] <= score[i-1]:
        x = score[i-1] - score[i] + 1
        score[i-1] -= x
        cnt += x

print(cnt)
