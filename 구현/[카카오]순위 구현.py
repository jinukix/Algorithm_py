## 정확성 통과
# def solution(info, query):

#     ans = []

#     for i in query:
#         cnt = 0
#         condition = i.split(' ')

#         if condition[0] == '-':
#             lang = ["cpp", "java", "python"]
#         else:
#             lang = condition[0]

#         if condition[2] == '-':
#             work = ["backend", "frontend"]
#         else:
#             work = condition[2]

#         if condition[4] == '-':
#             career = ["junior", "senior"]
#         else:
#             career = condition[4]

#         if condition[6] == '-':
#             food = ["chicken", "pizza"]
#         else:
#             food = condition[6]
            
#         score = int(condition[7])

#         for j in info:
#             j = j.split(' ')
#             if j[0] in lang and j[1] in work and j[2] in career and j[3] in food and int(j[4]) >= score:
#                 cnt += 1

#         ans.append(cnt)


    # return ans


## 정확성, 효율성 통과
from itertools import combinations
from collections import defaultdict

def solution(infos, queries):
    ans = []
    info_dict = defaultdict(list)

    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])

        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)

    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):
            query.remove('and')

        while '-' in query:
            query.remove('-')
        
        tmp_q = ''.join(query)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]

            if len(scores) > 0:
                start = 0
                end = len(scores)

                while end > start:
                    mid = (start + end) // 2

                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                ans.append(len(scores) - start)
        else:
            ans.append(0)

    return ans