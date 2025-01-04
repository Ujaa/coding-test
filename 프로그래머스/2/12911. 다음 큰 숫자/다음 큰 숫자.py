def solution(n):
    one_count = format(n, "b").count("1")
    while True:
        n += 1
        if one_count == format(n, "b").count("1"):
            return n