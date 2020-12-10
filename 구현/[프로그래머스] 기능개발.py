# ?? 왜 틀린지 모르겠음..

from collections import deque
from math import ceil


def solution(progresses, speeds):

    q = deque()
    answer = []

    for i in range(len(progresses)):
        x = ceil((100 - progresses[i]) / speeds[i])
        q.append(x)

    t = 0

    while q:
        t += q.popleft()
        cnt = 1

        while q:
            if t < q[0]:
                break

            q.popleft()
            cnt += 1

        answer.append(cnt)
    return answer


progresses = [99, 1]
speeds = [1, 99]
print(solution(progresses, speeds))
