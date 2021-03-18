import sys

def read():
    return sys.stdin.readline()


k = int(read())

data = [int(read()) for i in range(k)]
ans = []

for i in range(k):

    if data[i] != 0:
        ans.append(data[i])
    else:
        ans.pop()

print(sum(ans))
