import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    data.append(list(input().strip()))

alpha = [0 for i in range(26)]

for i in data:
    li = len(i)
    for j in range(li):
        alpha[ord(i[j]) - 65] += 10 ** (li - j - 1)

alpha.sort(reverse=True)

result = 0
cnt = 9

for i in alpha:
    result += cnt * i
    cnt -= 1

print(result)
