# def solution(n):

#     three = [0 for i in range(20)]

#     for i in range(20):
#         three[i] = (3**i)

#     threenum = 0

#     for i in range(19, -1, -1):
#         while n >= three[i]:
#             n -= three[i]
#             threenum += 10**i

#         if n == 0:
#             break

#     threenum = int(str(threenum)[::-1])
#     ans = 0

#     for i in range(19, -1, -1):
#         while threenum >= 10**i:
#             threenum -= 10**i
#             ans += three[i]

#         if threenum == 0:
#             break

#     return ans


def n_ary(n, base):
    result = []
    while n > 0:
        n, r = divmod(n, base)
        result.append(r)
    return ''.join(map(str, reversed(result)))


def solution(n):
    b3 = n_ary(n, 3)
    b3 = b3[::-1]
    return int(b3, 3)


n = 85

print(solution(n))
