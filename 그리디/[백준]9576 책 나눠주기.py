import sys


def read():
    return sys.stdin.readline().strip()


test = int(read())

for i in range(test):
    a, b = map(int, read().split())

    books = [False] * a

    data = []

    for j in range(b):
        v = list(map(int, read().split()))
        data.append(v)

    data.sort(key=lambda x: x[1])

    cnt = 0

    for j in range(len(data)):
        for k in range(data[j][0]-1, data[j][1]):
            if not books[k]:
                cnt += 1
                books[k] = True
                break

    print(cnt)
