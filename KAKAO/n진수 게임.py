def convert_numeral(num, base):
    q, r = divmod(num, base)
    n = '0123456789ABCDEF'[r]
    return convert_numeral(q, base) + n if q else n

def solution(n, t, m, p):
    convert_num = ''

    for i in range((p-1) + (m * (t-1))-1):
        convert_num += convert_numeral(i, n)
        
    ans = ''
    for i in range(t):
        idx = (p-1) + (m * i)
        ans += convert_num[idx]

    return ans