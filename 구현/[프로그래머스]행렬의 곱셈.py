def solution(arr1, arr2):
    arr = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                arr[i][j] += (arr1[i][k] * arr2[k][j])

    return arr