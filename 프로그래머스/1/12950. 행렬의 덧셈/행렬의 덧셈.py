def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        answer.append([a + b for a, b in zip(x, y)])
    return answer