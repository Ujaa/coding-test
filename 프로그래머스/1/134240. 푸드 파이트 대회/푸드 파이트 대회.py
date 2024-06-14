def solution(food):
    half = ''
    food = list(map(lambda x:x//2*2, food))
    for i, x in enumerate(food):
        half += str(i) * (x // 2)
    return half + "0" + half[::-1]