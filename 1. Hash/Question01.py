
def solution(participant, completion):
    fp = dict()
    for x in participant:
        if x in fp:
            fp[x] += 1
        else:
            fp[x] = 1
    for x in completion:
        fp[x] -= 1
    for answer, val in fp.items():
        if val == 1:
            print(answer)
            return answer


if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    solution(participant, completion)
