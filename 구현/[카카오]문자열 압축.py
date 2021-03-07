def solution(s):
    l = len(s)
    ans = []

    if len(s) == 1:
        return 1

    for i in range(1, l//2+1):
        cnt = 1
        tempStr = s[:i]
        result = ''

        for j in range(i, l, i):
            if s[j:j+i] == tempStr:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''

                result += str(cnt) + tempStr
                tempStr = s[j:j+i]
                cnt = 1

        if cnt == 1:
            cnt = ''

        result += str(cnt) + tempStr
        ans.append(len(result))
        
    return min(ans)
    