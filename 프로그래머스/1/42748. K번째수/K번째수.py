def solution(array, commands):
    answer = []
    for [x, y, z] in commands:
        answer.append(sorted(array[x-1:y])[z-1])
    return answer