n = int(input())
t = list(map(int, input().split()))

t.sort()

l = len(t)
sum = 0

for i in t:
    sum += i*l
    l -= 1

print(sum)
