def reverse_bracket(p):
    bracket = ''
    for i in p:
        if i == ')':
            bracket += '('
        else:
            bracket += ')'

    return bracket

def division_bracket(p):
    cnt = 0
    check = True
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1 
        else:
            cnt -= 1

        if cnt < 0:
            check = False

        if cnt == 0:
            u = p[:i+1]
            v = p[i+1:]

            if check:
                return u + division_bracket(v)
            else:
                return '('+ division_bracket(v) + ")" + reverse_bracket(u[1:-1])
                
    return p

def solution(p):
    return division_bracket(p)