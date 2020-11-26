n = int(input())
l = []

for i in range(n):
    start, end = map(int, input().split())
    l.append((start, end))

l.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0

for i in l:
    if i[0] >= end:
        cnt += 1
        end = i[1]

print(cnt)
