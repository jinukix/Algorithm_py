import sys


def read():
    return sys.stdin.readline().strip()


n, k = map(int, read().split())


def get_len(n):
    ans = 0
    start = 1
    l = 1

    while start <= n:
        end = start * 10 - 1

        if end >= n:
            ans += (n - start + 1) * l
        else:
            ans += (end - start + 1) * l

        start *= 10
        l += 1

    return ans


if get_len(n) < k:
    print(-1)
else:
    left = 1
    right = n
    res = 0

    while left <= right:
        mid = (left + right) // 2
        l = get_len(mid)

        if k > l:
            left = mid + 1
        else:
            res = mid
            right = mid - 1

    s = str(res)
    s_len = get_len(res)

    ans = s[len(s) - (s_len - k) - 1]
    print(ans)
