def solution(n):
    answer = 0
    converted = ""

    while n > 0:
        converted += str(n % 3)
        n = n // 3 
    
    for i, x in enumerate(converted[::-1]):
        answer += (3 ** i) * int(x)
    
    return answer
            