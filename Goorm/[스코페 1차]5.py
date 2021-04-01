import copy
from collections import deque
import sys

def read():
    return sys.stdin.readline().strip()

def bfs(temp, y, x, r):
    q = deque([[y, x, r]])

    while True:
        y, x, r = q.popleft()

        if y == m-1:
            return [int(temp[y][x]), r]

        if temp[y+1][x] != 'x':
            if temp[y][x] == 'c':
                temp[y+1][x] = 1
            else:
                print(y, x)
                print(temp[y][x])
                temp[y+1][x] = temp[y][x] +1

            q.append([y+1, x, r])
        else:
            if x+1 < n and temp[y][x+1] != 'x':
                if temp[y][x] == 'c':
                    temp[y][x+1] = 1
                else:
                    temp[y][x+1] = temp[y][x] +1
                
                q.append([y, x+1, r+1])

            if 0 <= x-1 and temp[y][x-1] != 'x':
                if temp[y][x] == 'c':
                    temp[y][x-1] = 1
                else:
                    temp[y][x-1] = temp[y][x] +1
                
                q.append([y, x-1, r+1])

    return



# n, m = map(int, read().split())
# graph = [list(read()) for _ in range(m)]

n = 4
m = 5
graph = [['c', 'c', 'c', 'c'], ['c', 'c', 'c', 'c'], ['x', 'x', '.', '.'], ['.', '.', '.', 'x'], ['x', '.', '.', 'x']]

dy = [-1, 0, 0]
dx = [0, -1, 1]
ans = []

for y in range(m):
    for x in range(n):
        temp = copy.deepcopy(graph)
        x = bfs(temp, y, x, 0) 
            
        if x:
            ans.append(x)

print(ans)
if ans:
    ans.sort(key = lambda x : x[0])
    print(ans[0][1])
else:
    print(-1)







"""
스크롤을 내릴 때 시선을 어디에 두는지?
가로 n 세로 m 화면

c : 시선이 시작
x : 비선호 컨텐츠
. : 선호 컨텐츠

x 를피해 .만 보면서 화면 최하단 까지 아래 + 좌우 방향으로만 이동 가능
좌우로 가장 적게 이동한 경로를 기준 경로

기준 경로를 찾아 좌우 이동한 횟수 출력.

4 5
c.xc
....
xx..
...x
x..x





"""