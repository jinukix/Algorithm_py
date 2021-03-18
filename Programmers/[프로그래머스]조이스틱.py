def solution(name):
    alpha = [min(ord(s) - ord('A'), ord('Z')-ord(s)+1) for s in name]
    idx = 0
    ans = 0

    while True:
        ans += alpha[idx]
        alpha[idx] = 0

        if sum(alpha) == 0:
            break
        
        left = 1
        right = 1

        while alpha[idx+right] == 0:
            right += 1

        while alpha[idx-left] == 0:
            left += 1
            
        if left >= right:
            idx += right
            ans += right
        else:
            idx -= left
            ans += left
    
    return ans