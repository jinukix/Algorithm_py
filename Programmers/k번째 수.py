def solution(array, commands):

    answer = []

    for i in range(len(commands)):
        a, b, c = commands[i]
        arr = array[a-1:b]
        arr.sort()
        answer.append(arr[c-1])

    return answer