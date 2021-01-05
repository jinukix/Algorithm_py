def solution(s):
    s = s.split(' ')
    answer = ''
    
    for word in s:
        for i in range(len(word)):
            answer += word[i].upper() if i % 2 == 0 else word[i].lower()
        answer += ' '

    return answer[:-1]

s = ""
print(solution(s))