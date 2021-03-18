def solution(s):
    
    s = s.replace('{', '').split('}')
    x = sorted(s, key = lambda x: len(x))
    
    ans = []
    
    for i in x:
        for j in i.split(','):
            if j.isdigit() and int(j) not in ans:
                ans.append(int(j))

    return ans