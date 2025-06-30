class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs=0
        gs=nums[0]
        for i in range(len(nums)):
            cs+=nums[i]
            gs=max(cs,gs)
            if cs<0:
                cs=0
        return gs