def solution(x):
    str_x= str(x)

    if x % sum([int(str_x[i]) for i in range(len(str_x))]) == 0:
        return True
    return False