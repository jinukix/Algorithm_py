import sys

def read():
    return sys.stdin.readline()

n = int(read())

w = list(map(int, read().split()))
w.sort()

minw = 1

for i in w:
    if minw >= i:
        minw += i
    else:
        break

print(minw)
