from itertools import permutations


def solution(numbers):

    per = []
    for i in range(1, len(numbers)+1):
        per.append(list(map(''.join, permutations(numbers, i))))

    nums = []
    answer = 0

    for i in per:
        for j in i:
            n = int(j)
            if n >= 2 and n not in nums:
                nums.append(n)
                answer += 1

    for i in nums:
        for j in range(2, i):
            if i % j == 0:
                answer -= 1
                break

    return answer
