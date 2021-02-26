# 문제를 잘못 이해한 풀이
'''
def solution(phone_book):
    cnt = len(phone_book)
    for i in range(cnt):
        for j in range(i + 1, cnt):
            if phone_book[i] in phone_book[j]:
                return False
    else:
        return True


if __name__ == "__main__":
    # phone_book = ["119", "97674223", "1195524421"]
    # phone_book = ["123", "456", "789"]
    phone_book = ["12", "123", "1235", "567", "88"]
    if solution(phone_book):
        print("True")
    else:
        print("False")
'''

# 답은 나오지만 해시를 사용하지 않음
'''
from collections import deque


def solution(phone_book):
    dq = deque(phone_book)
    cnt = len(phone_book)
    for _ in range(cnt):
        a = dq.popleft()
        for x in dq:
            if a in x:
                return False
        else:
            dq.append(a)
    else:
        return True


if __name__ == "__main__":
    # phone_book = ["119", "97674223", "1195524421"]
    # phone_book = ["123", "456", "789"]
    # phone_book = ["12", "123", "1235", "567", "88"]
    phone_book = ["113", "44", "4544"]
    if solution(phone_book):
        print("True")
    else:
        print("False")
'''


# 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return answer

if __name__ == "__main__":
    # phone_book = ["119", "97674223", "1195524421"]
    # phone_book = ["123", "456", "789"]
    # phone_book = ["12", "123", "1235", "567", "88"]
    phone_book = ["113", "44", "4544"]
    if solution(phone_book):
        print("True")
    else:
        print("False")
