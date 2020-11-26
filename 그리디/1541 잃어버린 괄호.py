data = list(input().split("-"))  # split("-") - 으로 구분.

num = []

for i in data:
    cnt = 0
    data = i.split('+')
    for j in data:
        cnt += int(j)
    num.append(cnt)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)
