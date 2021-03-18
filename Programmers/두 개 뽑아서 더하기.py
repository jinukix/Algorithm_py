def solution(numbers):

    s = set()
    l = len(numbers)

    for i in range(l):
        for j in range(i+1, l):
            s.add(numbers[i]+numbers[j])

    ans = list(s)
    ans.sort()

    return ans


numbers = [5, 0, 2, 7]

print(solution(numbers))
