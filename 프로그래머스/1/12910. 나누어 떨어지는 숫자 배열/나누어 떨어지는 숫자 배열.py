def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    return sorted(arr) if len(arr) > 0 else [-1]