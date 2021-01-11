from collections import deque


def solution(prices):
    q = deque(prices)
    answer = []

    while q:
        t = q.popleft()

        cnt = 0
        for i in q:
            cnt += 1
            if t > i:
                break

        answer.append(cnt)

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
