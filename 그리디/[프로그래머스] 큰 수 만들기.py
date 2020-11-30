
def solution(number, k):

    stack = [number[0]]

    for i in number[1:]:

        while len(stack) > 0 and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()

        stack.append(i)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)


# number = '417725284'
# k = 4
# print(solution(number, k))
