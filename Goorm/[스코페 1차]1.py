import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
t = [read() for _ in range(n)]

max_start = "0000"
min_end = "2400"

for i in t:
    i = i.split(" ~ ")

    start = i[0][:2] + i[0][3:]
    end = i[1][:2] + i[1][3:]

    if max_start < start:
        max_start = start

    if min_end > end:
        min_end = end

ans = -1
if max_start < min_end:
    ans = f"{max_start[:2]}:{max_start[2:]} ~ {min_end[:2]}:{min_end[2:]}"

print(ans)


"""


이용인원
각자 쏘카 존에 도착할 수 있는 시간
-> 모든 인원이 쏘카존에 올 수 있는 시간. > 그 시간에 빌릴 수 있는 자가용을 추천


3
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 20:00

14




"""