def solution(s):
    
    ans = f'{s[0].upper()}'

    for i in range(1, len(s)):

        if s[i-1] == ' ':
            ans += s[i].upper()
        else: #if s[i] != ' ':
            ans += s[i].lower()

    return ans