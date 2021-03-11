from collections import deque

def solution(n,a,b):
    ans = 0
    arr = [i+1 for i in range(n)]
    q = deque(arr)

    while q:
        x = q.popleft()
        y = q.popleft() 

        if (x == a or x == b) and (y == a or y == b):
            ans += 1
            break

        if y == a or y == b:
            q.append(y)
        else:
            q.append(x)

        if q[-1] == a:
            ans += 1

    return ans 