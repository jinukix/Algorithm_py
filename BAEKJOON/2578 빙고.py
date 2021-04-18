import sys


def read():
    return sys.stdin.readline().strip()


def initialize(bingo_size):
    graph = [list(map(int, read().split())) for i in range(bingo_size)]
    call_nums = []

    for _ in range(bingo_size):
        call_nums.extend(list(map(int, read().split())))

    return graph, call_nums


def solution(bingo_size, answer_count):
    graph, call_nums = initialize(bingo_size)

    bingo_cnt = 0
    call_cnt = 0

    for num in call_nums:
        call_cnt += 1
        for i in range(len(graph)):
            if num in graph[i]:
                idx = graph[i].index(num)
                graph[i][idx] = 0

                # 가로
                if sum(graph[i]) == 0:
                    bingo_cnt += 1

                # 세로
                for y in range(bingo_size):
                    if graph[y][idx] != 0:
                        break
                else:
                    bingo_cnt += 1

                # 대각선 \
                if idx == i:
                    for x in range(bingo_size):
                        if graph[x][x] != 0:
                            break
                    else:
                        bingo_cnt += 1

                # 대각선 /
                if idx + i == bingo_size - 1:
                    for x in range(bingo_size):
                        if graph[x][bingo_size-1-x] != 0:
                            break
                    else:
                        bingo_cnt += 1

                if bingo_cnt >= answer_count:
                    return call_cnt

                break


BINGO_SIZE = 5
ANSWER_COUNT = 3
ans = solution(BINGO_SIZE, ANSWER_COUNT)
print(ans)
