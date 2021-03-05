import sys

def read():
    return sys.stdin.readline().strip()


f = [0, 1]
for i in range(2, 50):
    f.append(f[i-1]+f[i-2])

t = int(read())
ans = []
for i in range(t):
    n = int(read())
    data = []

    for j in range(49, 0, -1):
        if n >= f[j]:
            n -= f[j]
            data.append(f[j])

    ans.append(data)

for i in range(t):
    for j in range(len(ans[i])-1, -1, -1):
        print(ans[i][j], end=" ")
    print()
