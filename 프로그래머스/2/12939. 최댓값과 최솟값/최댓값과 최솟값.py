def solution(s):
    nums_str = s.split()
    nums = list(map(int, nums_str))
    return f'{min(nums)} {max(nums)}'