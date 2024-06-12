def solution(sizes):
    w = 0
    h = 0
    
    for x in sizes:
        if w < min(x):
            w = min(x)
        if h < max(x):
            h = max(x)
    
    return w * h