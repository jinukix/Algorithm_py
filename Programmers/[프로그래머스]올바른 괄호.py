def solution(s):
    
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    return cnt == 0