import sys


def read():
    return sys.stdin.readline().strip()


# n, q = map(int, read().split())
n = 10
q = 6
# arr = [list(map(int, read().split())) for i in range(n - 1)]
# question = [list(map(int, read().split())) for i in range(q)]
arr = [[10, 9], [10, 8], [10, 7], [9, 1], [9, 2], [9, 3], [9, 4], [8, 5], [8, 6]]
question = [[10, 1], [10, 5], [8, 1], [1,10],[5,10],[3,3]]

parent = [[] for i in range(n + 1)]
child = [[] for i in range(n + 1)]

for a, b in arr:
    parent[b].append(a)
    child[a].append(b)

    for x in parent[a]:
        child[x].append(b)

for a, b in question:
    if b in child[a]:
        print("yes")
    else:
        print("no")

print(parent)
print(child)


"""

물품 = 단품 or 세트 or 패키지
단품을 조합해 하나의 세트로 포장 가능.
단품은 하나의 세트에만 포함
만들어진 세트는 또 다른 세트에 포함될 수 없음
패키지 = 세트 + 단품 and 다른 세트에 속하지 않는 최종 물품
포함관계 하위, 상위 물품 나뉨

시간?


"""
