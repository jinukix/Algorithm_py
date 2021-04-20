import sys


def read():
    return sys.stdin.readline().strip()


king, stone, n = map(str, read().split())
actions = [read() for i in range(int(n))]

king_y = int(king[1])
king_x = ord(king[0]) - 64
stone_y = int(stone[1])
stone_x = ord(stone[0]) - 64

move = {
    "R": [0, 1], "L": [0, -1], "B": [-1, 0], "T": [1, 0],
    "RT": [1, 1], "LT": [1, -1], "RB": [-1, 1], "LB": [-1, -1],
}

for action in actions:
    ky = king_y + move[action][0]
    kx = king_x + move[action][1]

    if 1 > ky or ky >= 9 or 1 > kx or kx >= 9:
        continue

    if ky == stone_y and kx == stone_x:
        sy = stone_y + move[action][0]
        sx = stone_x + move[action][1]

        if 1 > sy or sy >= 9 or 1 > sx or sx >= 9:
            continue

        stone_y = sy
        stone_x = sx

    king_y = ky
    king_x = kx

king = f"{chr(64 + king_x)}{str(king_y)}"
stone = f"{chr(64 + stone_x)}{str(stone_y)}"
print(king)
print(stone)
