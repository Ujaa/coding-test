def solution(price, money, count):
    req = price * count * (count + 1) / 2 - money
    return req if req >= 0 else 0