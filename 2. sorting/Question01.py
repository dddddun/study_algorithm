# 내가 푼 것
'''
def solution(array, commands):
    answer = []
    for case in commands:
        res = array[case[0] - 1:case[1]]
        res.sort()
        answer.append(res[case[2] - 1])
    print(answer)
    return answer
'''


# 탐나는 답안,,,
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i - 1:j])[k - 1])
    return answer


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))
