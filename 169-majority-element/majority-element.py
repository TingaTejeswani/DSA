class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==1:
            return nums[0]
        else:
            n=len(nums)//2
            return nums[n]