import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())

students = [list(read().split()) for i in range(n)]

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in students:
    print(i[0])
