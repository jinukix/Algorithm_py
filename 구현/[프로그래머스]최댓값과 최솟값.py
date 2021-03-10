def solution(s):
    s = s.split(' ')
    arr = []

    for i in s:
        arr.append(int(i))
        
    return f"{min(arr)} {max(arr)}"
    

s = "-1 -2 -3 -4"
print(solution(s))