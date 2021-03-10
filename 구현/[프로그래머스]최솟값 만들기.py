def solution(A,B):
    
    A.sort(reverse=True)
    B.sort()
    ans = 0
    for a, b in zip(A, B):
        ans += a * b

    return ans