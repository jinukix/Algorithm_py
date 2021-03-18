from collections import deque

def solution(maps):

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    n = len(maps)
    m = len(maps[0])

    def bfs(start_y, start_x):
        q = deque([(start_y, start_x)])
    
        while q:
            y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < n and 0 <= nx < m and not (start_y == ny and start_x == nx):
                    
                    if maps[ny][nx] == 1:
                        maps[ny][nx] = maps[y][x] + 1
                        q.append([ny, nx])

    bfs(0, 0)
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]