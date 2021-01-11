def solution(n, stages):

    lv = [[0, 0] for i in range(n)]

    for i in range(n):
        deno, mole = 0, 0
        for j in stages:
            if i+1 <= j:
                deno += 1

                if i+1 == j:
                    mole += 1

        if deno == 0:
            lv[i] = [0, i]
        else:
            lv[i] = [mole/deno, i]

    lv.sort(key=lambda x: (-x[0], x[1]))

    ans = []

    for i in range(n):
        ans.append(lv[i][1]+1)

    return ans


n = 8
stages = [1, 2, 3, 4, 5, 6, 7]

print(solution(n, stages))
