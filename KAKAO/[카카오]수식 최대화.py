from itertools import permutations

def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n+1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    ans = 0
    signs = list(permutations("+-*"))

    for sign in signs:
        res = int(calc(sign, 0, expression))
        ans = max(ans, abs(res))
    
    return ans