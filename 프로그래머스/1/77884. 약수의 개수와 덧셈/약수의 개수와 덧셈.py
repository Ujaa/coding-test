def solution(left, right):
    answer = 0
    
    for x in range(left, right + 1):
        if x ** (1/2) == int(x ** (1/2)):
            answer -= x
        else:
            answer += x
    
    return answer