def dropblock(maps, y, x):
    for i in range(y-1, -1, -1):
        for j in range(x):
            if maps[i][j] == '0':
                for k in range(i, -1, -1):
                    if maps[k][j] != '0':
                        maps[i][j], maps[k][j] = maps[k][j], maps[i][j]
                        break

def boomblock(maps, y, x):
    cnt = 0 

    for i in range(y, y+2):
        for j in range(x, x+2):
            if maps[i][j] != '0':
                maps[i][j] = '0'
                cnt += 1

    return cnt

def checkblock(maps, y, x):
    ch = maps[y][x]
    for i in range(y, y+2):
        for j in range(x, x+2):
            if ch != maps[i][j]:
                return False

    return True

def solution(m, n, board):
    maps = [[] for i in range(m)]

    for i in range(m):
        maps[i] = list(board[i])

    isCheck = True
    ans = 0

    while isCheck:
        isCheck = False
        check = []
        for y in range(m-1):
            for x in range(n-1):
                if maps[y][x] != '0' and checkblock(maps, y, x):
                    check.append([y, x])
                    isCheck = True

        for y, x in check:
            ans += boomblock(maps, y, x)

        dropblock(maps, m, n)

    return ans

board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
n = 6
m = 6

print(solution(m, n, board))