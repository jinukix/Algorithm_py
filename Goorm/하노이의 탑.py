n = int(input())
ans = []

# n개의 블럭을 a에서 b를거쳐 c로 옮기기.
def move(n, a, b, c):
    if n == 1:
        ans.append([a, c])
    else:
        move(n - 1, a, c, b)
        ans.append([a, c])
        move(n - 1, b, a, c)
