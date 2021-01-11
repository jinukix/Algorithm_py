def solution(arr, divisor):

    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if answer == []:
        return [-1]
    answer.sort()
    return answer


arr = [5, 9, 7, 10]
divisor = 5


print(solution(arr, divisor))
