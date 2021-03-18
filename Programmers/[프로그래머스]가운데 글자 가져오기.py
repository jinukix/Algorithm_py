def solution(s):

    l = len(s)
    if l % 2 == 1:
        return s[l//2]
    else:
        return s[l//2-1] + s[l//2]


s = "abcde"
print(solution(s))
