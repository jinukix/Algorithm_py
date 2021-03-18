def solution(n):
    ans = 1

    for i in range(1, n//2 +1):
        cnt = 0

        for j in range(i, n):
            cnt += j
            if cnt == n:
                ans += 1
                break
            elif cnt > n:
                break

    return ans
