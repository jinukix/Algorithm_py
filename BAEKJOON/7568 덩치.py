import sys


def read():
    return sys.stdin.readline()


n = int(read())

data = [list(map(int, read().split())) for i in range(n)]
rank = [1 for i in range(n)]


for i in range(n):
    w = data[i][0]
    h = data[i][1]

    for j in range(i, n):

        # i보다 j가 몸무게도 크고 키도 클때 (덩치가 크다면) i의 등수 + 1
        if w < data[j][0] and h < data[j][1]:
            rank[i] += 1

        # i보다 j가 덩치가 작다면 j의 등수 + 1
        if w > data[j][0] and h > data[j][1]:
            rank[j] += 1


for i in rank:
    print(i, end=" ")
