def solution(citations):

    ans = 0
    l = len(citations)

    for i in range(1, 10001):
        cnt = 0
        for j in citations:
            if i <= j:
                cnt += 1
        if cnt >= i and l - cnt <= i:
            ans = i
        else:
            break

    return ans
