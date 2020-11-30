def solution(name):

    alpha = [min(ord(s) - ord('A'), ord('Z')-ord(s)+1) for s in name]

    answer = 0
    locat = 0

    print(alpha)

    while True:
        answer += alpha[locat]
        alpha[locat] = 0

        if sum(alpha) == 0:
            break

        left = 1
        right = 1

        # 현재 A가 아닌 문자가 어느쪽에 더 가까운가 만 보기.

        while alpha[locat+right] == 0:
            right += 1

        while alpha[locat-left] == 0:
            left += 1

        if left >= right:
            locat += right
            answer += right
        else:
            locat -= left
            answer += left

    return answer


name = 'JEROEN'

print(solution(name))
