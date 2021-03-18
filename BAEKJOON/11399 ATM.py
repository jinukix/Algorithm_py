import sys

def read():
    return sys.stdin.readline().strip()


n = int(read())
t = list(map(int, read().split()))

t.sort()

l = len(t)
sum = 0

for i in t:
    sum += i * l
    l -= 1

print(sum)
