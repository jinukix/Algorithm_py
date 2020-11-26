import sys
input = sys.stdin.readline

n = int(input())

w = []
w = list(map(int, input().split()))

w.sort()

minw = 1

for i in w:
    if minw >= i:
        minw += i
    else:
        break

print(minw)
