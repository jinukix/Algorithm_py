from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    dict = defaultdict(int)
    for order in orders:
        for i in course:
            for j in list(combinations(order, i)):
                j = ''.join(sorted(j))
                dict[j] += 1

    li = []
    for key, value in dict.items():
        if value >= 2:
            li.append([value, key])
        
    li.sort(reverse=True)
    ans = []
    for i in course:
        max_cnt = -1
        for j in li:
            if i == len(j[1]):
                if max_cnt == -1:
                    max_cnt = j[0]

                if max_cnt == j[0]:
                    ans.append(j[1])

                if max_cnt > j[0]:
                    break
    
    ans.sort()
    return ans