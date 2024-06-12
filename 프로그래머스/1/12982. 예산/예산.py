def solution(d, budget):
    step = 0
    d.sort()
    
    for x in d:
        if budget - x < 0:
            break
        budget = budget - x
        step += 1
    
    return step