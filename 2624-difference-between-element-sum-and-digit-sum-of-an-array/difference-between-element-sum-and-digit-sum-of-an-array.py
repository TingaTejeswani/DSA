class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        b=0
        for i in nums:
            for j in str(i):
                b=b+int(j)
        return abs(sum(nums)-b)