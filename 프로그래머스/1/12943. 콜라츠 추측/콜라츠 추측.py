def solution(num):
    step = 0
    
    if num == 1:
        return step
    
    while step < 500:
        if num == 1:
            return step
        
        if num % 2 == 0:
            num = num // 2
            step += 1
            continue
            
        if num % 2 == 1:
            num = num * 3 + 1
            step += 1
            continue
            
    return -1
        

        