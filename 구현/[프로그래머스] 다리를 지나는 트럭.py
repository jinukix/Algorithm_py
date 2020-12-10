from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while q:
        time += 1
        q.popleft()

        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.popleft())
            else:
                q.append(0)

    return time


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
