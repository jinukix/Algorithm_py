def solution(n):
    ans = 0

    while True:
        if n <= 0:
            break

        q, r = divmod(n, 2)
        n = q
        ans += r

    return ans