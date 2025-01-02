def solution(s):
    stack = []
    try:
        for l in s:
            if l == "(":
                stack.append(l)
            else:
                stack.pop()
    except Exception as e:
        return False
    
    return len(stack) == 0