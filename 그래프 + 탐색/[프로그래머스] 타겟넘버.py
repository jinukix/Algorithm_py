def DFS(numbers, target, value, idx):

    global answer
    l = len(numbers)

    if l == idx:
        if value == target:
            answer += 1
        return

    DFS(numbers, target, value + numbers[idx], idx+1)
    DFS(numbers, target, value - numbers[idx], idx+1)


def solution(numbers, target):
    global answer
    answer = 0
    DFS(numbers, target, 0, 0)
    return answer
