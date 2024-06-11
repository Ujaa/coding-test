class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하기
        nums.sort()
        return sum([min([nums[x], nums[x+1]]) for x in range(0, len(nums)-1, 2)])