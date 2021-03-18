def solution(routes):

    routes.sort(key=lambda x: x[0])

    cnt = 1

    start = routes[0][0]
    end = routes[0][1]

    for i in range(1, len(routes)):

        if not (start <= routes[i][0] <= end or start <= routes[i][1] <= end):
            cnt += 1
            start = routes[i][0]
            end = routes[i][1]
            continue

        if start < routes[i][0]:
            start = routes[i][0]

        if end > routes[i][1]:
            end = routes[i][1]

    return cnt


routes = [[0, 1], [2, 3], [4, 5], [6, 7]]
print(solution(routes))
