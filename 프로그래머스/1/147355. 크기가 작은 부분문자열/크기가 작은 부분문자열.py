def solution(t, p):
    count = 0
    for x in range(len(t) - len(p) + 1):
        if t[x:x + len(p)] <= p:
            count += 1
    
    return count