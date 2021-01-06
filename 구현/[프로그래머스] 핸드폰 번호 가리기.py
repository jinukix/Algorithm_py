def solution(phone_number):
    l = len(phone_number)
    
    return '*' * (l-4) + phone_number[(l-4):]
    