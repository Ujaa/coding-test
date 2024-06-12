def solution(t, p):
    count = 0
    
    for x in range(len(t) - len(p) + 1):
        if int(t[x:x + len(p)]) <= int(p):
            count += 1
    
    return count