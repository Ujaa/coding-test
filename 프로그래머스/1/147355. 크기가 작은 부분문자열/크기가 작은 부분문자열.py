def solution(t, p):
    count = 0
    for i in range(len(t) - len(p) + 1):
        str = t[i:i+len(p)]
        if int(str) <= int(p):
            count += 1

    return count