def solution(new_id):
    ans = ''
    for ch in new_id:
        if ch.isalpha():
            ans += ch.lower()
        
        if ch.isdigit() or ch in "-_.":
            ans += ch

    while '..' in ans:
        ans = ans.replace("..", '.')

    ans = ans.strip('.')

    if not ans:
        ans = 'a'

    if len(ans) >= 16:
        ans = ans[:15]
        ans = ans.strip('.')

    while len(ans) < 3:
        ans += ans[-1]

    return ans


new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))