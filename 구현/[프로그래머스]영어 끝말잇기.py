def solution(n, words):
    arr = [words[0]]
    ans = [0, 0]

    for i in range(1, len(words)):
        if words[i] in arr or arr[-1][-1] != words[i][0]:
            ans = [(i%n)+1, (i // n) +1] 
            break
        
        arr.append(words[i])

    return ans