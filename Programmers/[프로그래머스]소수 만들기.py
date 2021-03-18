from itertools import combinations

def solution(nums):
    ans = 0
    for n in list(combinations(nums, 3)):
        s = sum(n)
        for j in range(2, int(s ** 0.5) + 1):
            if s % j == 0:
                break
        else:
            ans += 1
            
    return ans