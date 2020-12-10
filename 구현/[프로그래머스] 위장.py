from collections import Counter


def solution(clothes):
    arr = []

    for i in range(len(clothes)):
        arr.append(clothes[i][1])

    cnt = 0
    for i in Counter(arr).values():
        cnt *= i + 1
        cnt += i

    return cnt
