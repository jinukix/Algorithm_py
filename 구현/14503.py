import sys


def read():
    return sys.stdin.readline()


n, m = map(int, read().split())

y, x, dir = map(int, read().split())

map = [list(map(int, read().split()))for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0
ans = 0


while True:
    # print(f"현재 위치 : [{y}][{x}] 방향 : {dir}")

    if map[y][x] == 0:
        ans += 1
        map[y][x] = 2
        # print(f"청소완료! : [{y}][{x}]")

    if cnt == 4:
        ny = y - dy[dir]
        nx = x - dx[dir]

        if (ny < 0 and ny > n) and (nx < 0 and nx > m) or map[ny][nx] == 1:
            # print("break")
            break
        else:
            y = ny
            x = nx
            cnt = 0
            # print("뒤로이동")

    cnt += 1
    dir -= 1
    if dir == -1:
        dir = 3

    ny = y + dy[dir]
    nx = x + dx[dir]

    if (ny < 0 and ny > n) and (nx < 0 and nx > m) or map[ny][nx] == 1 or map[ny][nx] == 2:
        pass
    else:
        cnt = 0
        y = ny
        x = nx


print(ans)
# print(map)
