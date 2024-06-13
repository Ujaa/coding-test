def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for l in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[l])
    return sorted(list(answer))