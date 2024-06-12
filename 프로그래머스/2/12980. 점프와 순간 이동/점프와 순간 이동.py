def solution(n):
    step = 0

    if n == 1:
        return 1
    
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            step += 1
    
    return step