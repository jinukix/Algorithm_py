import sys

def read():
    return sys.stdin.readline().strip()

r, c = map(int, read().split())
maps = []

for i in range(r):
    arr = list(read().strip())
    maps.append(arr)

dirs = [(-1, 1), (0, 1), (1, 1)]
end_line = len(maps[0]) - 1

def connect_pipe(y, x):
    maps[y][x] = 'x'
    if x == end_line:
        return True

    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == ".":
            if connect_pipe(ny, nx):
                return True
    return False

ans = 0
for y in range(len(maps)):
    if connect_pipe(y, 0):
        ans += 1

print(ans)
