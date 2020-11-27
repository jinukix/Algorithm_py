"""
분리 집합이란 중복 포함된 원소가 없는 집합이다.

분리 집합 자료구조 : 분리 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조.

분리 집합 자료구조를 구현할 때는 트리 자료구조를 이용해 집합을 표현하는데,
기존 트리 구조와는 달리 자식 노드가 부모 노드를 가리키는 형태이다.

분리 집합 탐색 연산은 해당 원소 노드가 속해 있는 집합, 즉 루트 노드를 찾는 연산이다.
분리 집합에선 자식이 부모를 가리키므로 가리키는 부모를 따라 이동하다 보면 루트 노드에 도착하게 된다. 
그 루트 노드를 반환하면 해당 원소 노드가 속해 있는 집합을 알 수 있다. 

Union - Find 두 연산을 사용해 분리 집합 자료구조를 다룰수있다.

union (합집합) : 두 집합을 하나로 합친다. (A의 부모를 B의 부모로 설정하는 것.)
find (집합 탐색) : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산. (즉 루트 노드를 찾는 연산)

"""

import sys


def read():
    return sys.stdin.readline().strip()


def find_parnet(parent, x):
    if parent[x] != x:
        parent[x] = find_parnet(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parnet(parent, a)
    b = find_parnet(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, read().split())
parent = [0 for i in range(v+1)]

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, read().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합 : ", end=" ")
for i in range(1, v+1):
    print(find_parnet(parent, i), end=" ")

print()

print("부모 테이블 : ", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")

"""
입력
6 4
1 4
2 3
2 4
5 6

출력

각 원소가 속한 집합 :  1 1 1 1 5 5 
부모 테이블 :  1 1 2 1 5 5 

"""
