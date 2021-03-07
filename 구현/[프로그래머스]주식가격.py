def solution(prices):
    l = len(prices)
    ans = [0 for i in range(l)]

    for i in range(l-1):
        cnt = 0

        for j in range(i+1, l):
            cnt+=1

            if prices[i] > prices[j]:
                break
            
        ans[i] = cnt

    return ans