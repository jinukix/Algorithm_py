from collections import deque


def solution(bridge_length, weight, truck_weights):

    bridge = deque([0 for i in range(bridge_length)])
    time = 0
    current_w = 0

    while bridge:
        time+=1
        current_w -= bridge[0]
        bridge.popleft()

        if truck_weights:
            if truck_weights[-1] + current_w <= weight:
                current_w += truck_weights[-1]
                bridge.append(truck_weights.pop())
            else:
                bridge.append(0)

    return time
            

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
