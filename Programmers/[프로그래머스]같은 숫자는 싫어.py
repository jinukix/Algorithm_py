def solution(arr):

    ans = []
    s = arr[0]
    for i in range(1, len(arr)):

        if s != arr[i]:
            ans.append(s)
            s = arr[i]

    ans.append(s)

    return(ans)


arr = [1, 1, 3, 3, 0, 1, 1]

print(solution(arr))
