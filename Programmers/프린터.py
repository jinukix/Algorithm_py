def solution(priorities, location):
    
    cnt = 0
    idx = 0
    
    while True:
        if priorities[idx] == max(priorities):
            cnt+=1
            priorities[idx] *= -1
            
            if idx == location:
                return cnt

        idx+=1
        if idx == len(priorities):
            idx = 0

priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities, location))