def code(c, n):
    if c.isupper():
        if ord(c) + n - 90  > 0:
            return chr(64 + ord(c) + n - 90)
        else:
            return chr(ord(c) + n)
    elif c.islower():
        if ord(c) + n - 122  > 0:
            return chr(96 + ord(c) + n - 122)
        else:
            return chr(ord(c) + n)
    else:
        return " "

def solution(s, n):
    return "".join(map(lambda x:code(x, n), list(s)))

