class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gs=nums[0]
        cs=0
        for i in nums:
            cs+=i
            gs=max(gs,cs)
            if cs<0:
                cs=0
        return gs            