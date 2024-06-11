def solution(n):
    return int(''.join(sorted([x for x in str(n)], reverse=True)))
