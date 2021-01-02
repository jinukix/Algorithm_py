def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


def solution(n, m):
    return [gcd(n, m), n*m/gcd(n, m)]
