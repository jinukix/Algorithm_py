import sys


def read():
    return sys.stdin.readline().strip()


n, k = map(int, read().split())
data = list(map(int, read().split()))
m = [0 for i in range(n)]
cnt = 0

for i in range(k):
    isTrue = False
    for j in range(n):
        if m[j] == data[i] or m[j] == 0:
            isTrue = True
            m[j] = data[i]
            break
    if isTrue:
        continue
    else:
        a = 0
        for j in range(n):
            try:
                if a < data[i+1:].index(m[j]):
                    a = data[i+1:].index(m[j])
                    b = j
            except:
                b = j
                break
        m[b] = data[i]
        cnt += 1

print(cnt)
