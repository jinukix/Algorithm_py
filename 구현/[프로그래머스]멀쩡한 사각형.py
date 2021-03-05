def gcx(x, y):
    while y:
        x, y = y, x % y
    return x

def solution(w,h):
    return w*h - (w+h - gcx(w,h))
