def solution(n, lost, reserve):

    answer = 0
    student = [1 for i in range(n)]

    for i in lost:
        student[i-1] -= 1

    for i in reserve:
        student[i-1] += 1

    for i in range(n):
        if student[i] == 0:

            if i != 0 and student[i-1] == 2:
                student[i] += 1
                student[i-1] -= 1
            elif i != n-1 and student[i+1] == 2:
                student[i] += 1
                student[i+1] -= 1

        if student[i] != 0:
            answer += 1

    return answer


a = 5
b = [2, 4]
c = [3]
print(solution(a, b, c))
