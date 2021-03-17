def solution(msg):
    alpha = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ans = []
    idx = 0

    while True:
        ch = ''
        
        while idx < len(msg) and ch + msg[idx] in alpha:
            ch += msg[idx]
            idx += 1

        if ch == '':
            break
        
        ans.append(alpha.index(ch))

        if idx < len(msg):
            alpha.append(ch+msg[idx])

    return ans