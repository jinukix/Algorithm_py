import sys


def read():
    return sys.stdin.readline()


n = int(read())
k = int(read())

board = [[0 for i in range(n)] for i in range(n)]

for i in range(k):  # 사과 입력
    a, b = map(int, read().split())
    board[a-1][b-1] = 1

l = int(read())

command = []
command_num = 0
for _ in range(l):  # 명령 입력
    a, b = read().split()
    a = int(a)
    command.append([a, b])


dir = 0
y, x = 0, 0
dy = [0, 1, 0, -1]  # 동남서북
dx = [1, 0, -1, 0]

snake = [[0, 0]]
t = 0

while True:

    for i in range(len(snake)):
        board[snake[i][0]][snake[i][1]] = 0

    y = y+dy[dir]
    x = x+dx[dir]

    if (0 > y or n <= y) or (0 > x or n <= x):  # 벽에 부딪
        break
    if [y, x] in snake:  # 뱀 꼬리 부딪
        break

    if board[y][x] == 1:  # 사과일 떄
        board[y][x] = 0
    else:
        snake.pop(0)

    snake.append([y, x])
    t += 1

    for i in range(len(snake)):
        board[snake[i][0]][snake[i][1]] = 2

    if command_num < len(command) and t >= command[command_num][0]:
        if command[command_num][1] == 'D':
            dir += 1
            if dir > 3:
                dir = 0
        if command[command_num][1] == 'L':
            dir -= 1
            if dir < 0:
                dir = 3
        command_num += 1

    # 시뮬레이션
    # print(f"현재시간 : {t} 방향 : {dir}")
    # for i in range(n):
    #     print(board[i])

    # print("snake : ", snake)

    # print()


print(t+1)
