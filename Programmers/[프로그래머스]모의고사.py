def solution(answers):

    score = {}

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score[1] = 0
    score[2] = 0
    score[3] = 0

    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            score[1] += 1
        if answers[i] == b[i % len(b)]:
            score[2] += 1
        if answers[i] == c[i % len(c)]:
            score[3] += 1

    answer = []

    for key, value in score.items():
        if value == max(score[1], score[2], score[3]):
            answer.append(key)

    return answer
