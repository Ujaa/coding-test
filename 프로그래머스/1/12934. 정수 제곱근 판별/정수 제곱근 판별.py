def solution(n):
    root = n**(1/2)
    return (root + 1)**2 if int(root) == root else - 1