import sys


def read():
    return sys.stdin.readline().strip()


while True:
    n = str(read())

    if n == '0':
        break

    if n == n[::-1]:
        print("yes")
    else:
        print("no")