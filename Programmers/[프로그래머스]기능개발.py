import math

def solution(progresses, speeds):
    li = []
    time = 0
    ans = []
    
    for i in range(len(progresses)):
        li.append(math.ceil((100 - progresses[i]) / speeds[i]))

    for i in range(len(li)):

        if time < li[i]:
            time += (li[i] - time)
            ans.append(1)
        else:
            ans[-1] += 1

    return ans