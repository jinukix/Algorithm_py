import itertools

def solution(n):
    map = [[0 for _ in range(1, i+1)] for i in range(1, n+1)]
    y = -1; x = 0
    num = 1

    # 아래, 오른쪽, 대각선(위 + 왼쪽)
    dy = [1, 0, -1]
    dx = [0, 1, -1]

    for i in range(n):
        for _ in range(i, n):
            idx = i % 3 

            y = y + dy[idx]
            x = x + dx[idx]

            map[y][x] = num
            num += 1
            
    ans = list(itertools.chain(*map))

    return ans