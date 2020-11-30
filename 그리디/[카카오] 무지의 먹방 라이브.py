# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))  # (음식시간, 음식번호)

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간.

    lenght = len(food_times)

    while sum_value + ((q[0][0] - previous) * lenght) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*lenght
        lenght -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value) % lenght][1]


# a = [3, 1, 2]
# k = 5
# print(solution(a, k))
