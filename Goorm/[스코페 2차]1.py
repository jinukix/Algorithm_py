import sys


def read():
    return sys.stdin.readline().strip()


n, t = read().split()
t = t.split(":")
time = (60 * 60 * int(t[0])) + (60 * int(t[1])) + int(t[2])

l = [read() for i in range(int(n))]
play = []
for i in l:
    i = i.split(":")
    play.append(60 * int(i[0]) + int(i[1]))

ans = []

for i in range(len(play)):
    s = play[i]
    cnt = 1
    for j in range(i + 1, len(play)):
        if s >= time:
            ans.append(cnt)
            break

        s += play[j]
        cnt += 1

m = max(ans)
print(m, ans.index(m) + 1)

"""
특정 장르를 무작위로 선정 -> 음악 재생
플레이리스트가 끝날 때 까진 노래에 맞춰 춤을 춤.


- 한 번 재생 멈추기 x
- 처음 만들어진 순서대로 재생, 순서변경x
- 최대한 많은 음악 플레이, 총 시간길더라도 더 많은 곡 연습.
"""