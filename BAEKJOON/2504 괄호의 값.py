import sys


def read():
    return sys.stdin.readline().strip()


brackets = read()
stack = []

for bracket in brackets:
    if bracket == ')':
        temp = 0

        while stack:
            top = stack.pop()

            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif top == '[':
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = top
                else:
                    temp = temp + top

    elif bracket == ']':
        temp = 0

        while stack:
            top = stack.pop()

            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif top == '(':
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = top
                else:
                    temp = temp + top

    else:
        stack.append(bracket)


if "(" in stack or "[" in stack:
    print(0)
else:
    print(sum(stack))
