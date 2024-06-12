def solution(arr):
    answer = []
    before = -999
    
    for x in arr:
        if before != x:
            answer.append(x)
        before = x 
        
    return answer