# HASH

def solution(phone_book):

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):

            l = min(len(phone_book[i]), len(phone_book[j]))

            if phone_book[i][:l] == phone_book[j][:l]:
                return False

    return True
