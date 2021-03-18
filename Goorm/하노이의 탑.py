n = int(input())
ans = []

def move(n, a, b, c):
    if n == 1:
        ans.append([a, c])
    else:
        move(n-1, a, c, b)
        ans.append([a, c])
        move(n-1, b, a, c)

move(n, 1, 2, 3)
print(ans)
print(len(ans))