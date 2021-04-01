def solution(numbers):
    n = [str(x) for x in numbers]
    n.sort(key=lambda x: x * 2, reverse=True)
    answer = str(int("".join(n)))
    return answer