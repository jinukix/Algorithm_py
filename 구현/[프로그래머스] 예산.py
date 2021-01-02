def solution(d, budget):
    d.sort()

    cnt = 0
    for i in d:

        if budget >= i:
            budget -= i
            cnt += 1
        else:
            break

    return cnt


d = [1, 3, 2, 5, 4]
budget = 9

print(solution(d, budget))
