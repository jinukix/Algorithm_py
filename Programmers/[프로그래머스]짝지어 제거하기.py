def solution(s):
    arr = []

    for i in s:
        if len(arr) > 0 and arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)

    if len(arr):
        return 0
    else:
        return 1


s = "baabaa"
print(solution(s))

