def solution(n, arr1, arr2):

    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])[2:]
        arr1[i] = (n-len(arr1[i]))*'0' + arr1[i]

        arr2[i] = bin(arr2[i])[2:]
        arr2[i] = (n-len(arr2[i]))*'0' + arr2[i]

    answer = ['' for i in range(n)]

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
