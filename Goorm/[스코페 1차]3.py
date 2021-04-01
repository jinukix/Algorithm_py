import sys


def read():
    return sys.stdin.readline().strip()


def find_square(y, x, r):
    for dy in range(y, y + r):
        for dx in range(x, x + r):
            if maps[dy][dx] == "0":
                return False

    return True


n = int(read())
maps = [read() for i in range(n)]

size = [0 for i in range(n + 1)]
ans = 0

for r in range(1, n + 1):
    for y in range(n - r + 1):
        for x in range(n - r + 1):
            if maps[y][x] == "0":
                continue

            if find_square(y, x, r):
                size[r] += 1
                ans += 1

print(f"total: {ans}")

for i in range(1, len(size)):
    if size[i] != 0:
        print(f"size[{i}]: {size[i]}")


"""

사용자의 공간정보를 올리면 각 공간에 대한 상품 추천 기능.

공간에 상품을 놓을 수 있는 경우의 수

- 입력되는 공간 정보 1 정사각형
- 공간은 가로, 세로 1인 정사각형 모양 여러개로 구성
- 상품은 항상 정사각형 크기로 배치, 까만 곳만 배치 가능 검게 칠해짐 : 1

1110
0110
0000





"""