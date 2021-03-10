def solution(s):
    zero = 0
    cnt = 0

    while s != '1':
        l = len(s)
        s = s.replace('0', '')
        zero += l - len(s)
        s = bin(len(s))[2:]
        cnt += 1

    return [cnt, zero]


s = "110010101001"
print(solution(s))