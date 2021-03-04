import sys

def read():
    return sys.stdin.readline()

data = read().split("-")
ans  = 0

for i in data[0].split("+"):
    ans += int(i)

for i in data[1:]:
    minus = i.split("+")
    l = len(minus)
    for j in range(l):
        ans -= int(minus[j])

print(ans)
