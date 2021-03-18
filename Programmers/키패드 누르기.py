def solution(numbers, hand):

    left_pos = (3, 0)
    right_pos = (3, 2)

    answer = ''
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            left_pos = (i//3, 0)
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            right_pos = (i//4, 2)
        else:
            if i == 0:
                click_pos = (3, 1)
            else:
                click_pos = (i//4, 1)

            l_l = (abs(click_pos[0]-left_pos[0]) +
                   abs(click_pos[1]-left_pos[1]))

            r_l = (abs(click_pos[0]-right_pos[0]) +
                   abs(click_pos[1]-right_pos[1]))

            if l_l < r_l:
                answer += "L"
                left_pos = click_pos
            elif l_l > r_l:
                answer += "R"
                right_pos = click_pos
            else:
                if hand == 'right':
                    answer += "R"
                    right_pos = click_pos
                else:
                    answer += "L"
                    left_pos = click_pos

    return answer
