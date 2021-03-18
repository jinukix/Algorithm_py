def solution(dirs):
    y, x = 0, 0 

    dict = {}
    dict['U'] = [1, 0]
    dict['D'] = [-1, 0]
    dict['R'] = [0, 1]
    dict['L'] = [0, -1]
    cnt = 0
    load = []

    for i in dirs:
        dy, dx = dict[i]

        ny = y + dy
        nx = x + dx

        if -5 <= ny <= 5 and -5 <= nx <= 5:
            if [y, x, ny, nx] not in load and [ny, nx, y, x] not in load:
                load.append([y, x, ny, nx])
                cnt += 1

            y = ny
            x = nx
            
    return cnt