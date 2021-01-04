
def solution(array, commands):

    answer = []

    for i in range(len(commands)):
        a, b, c = commands[i]
        arr = array[a-1:b]
        arr.sort()
        answer.append(arr[c-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
