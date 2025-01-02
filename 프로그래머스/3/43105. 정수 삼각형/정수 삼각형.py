def solution(triangle):
    for li, line in enumerate(triangle):
        if li == 0:
            continue
            
        for ni, n in enumerate(line):
            if ni == 0:
                triangle[li][ni] += triangle[li - 1][ni]
            elif ni == len(line) - 1:
                triangle[li][ni] += triangle[li - 1][ni - 1]
            else: 
                left = triangle[li - 1][ni - 1]
                right = triangle[li - 1][ni]
                if left > right:
                    triangle[li][ni] += left
                else:
                    triangle[li][ni] += right

    return max(triangle[-1])