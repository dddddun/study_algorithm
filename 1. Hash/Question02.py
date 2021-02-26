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
