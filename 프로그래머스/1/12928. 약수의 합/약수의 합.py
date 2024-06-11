def solution(n):
    nums = []

    for x in range(1, n+1):
        if n % x == 0:
            nums.append(x)
            
    return sum(nums)
        
