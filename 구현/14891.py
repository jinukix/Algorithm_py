import sys


def read():
    return sys.stdin.readline()


def rotate_clock(num, dir, v):

    v[num] = True

    r = gear[num][2]
    l = gear[num][6]

    if dir == 1:
        gear[num] = gear[num][-1] + gear[num][:-1]
    elif dir == -1:
        gear[num] = gear[num][1:] + gear[num][0]

    if num != 3 and v[num+1] == False:
        if r != gear[num+1][6]:
            rotate_clock(num+1, dir*-1, v)

    if num != 0 and v[num-1] == False:
        if l != gear[num-1][2]:
            rotate_clock(num-1, dir*-1, v)


gear = [0 for i in range(4)]

for i in range(4):
    gear[i] = read().rstrip()


k = int(read())

rot = [list(map(int, read().split())) for i in range(k)]


for i in range(k):

    v = [False for i in range(4)]

    num = rot[i][0] - 1
    dir = rot[i][1]

    rotate_clock(num, dir, v)


ans = 0

for i in range(4):
    if gear[i][0] == '1':
        ans += 2 ** i

print(ans)
