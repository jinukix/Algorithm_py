def maxProfit(prices): 

    max_num = 0

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            num = prices[j]-prices[i]

            if max_num < num:
                max_num = num
    
    return max_num




prices = [7,6,4,3,1]
print(maxProfit(prices))