class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=1
        n=len(nums)
        h=n-1
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        while l<=h:
            m=(l+h)//2
            if nums[m]!=nums[m+1] and nums[m]!=nums[m-1]:
                return nums[m]
            elif m%2==0 and nums[m]==nums[m+1] or m%2==1 and nums[m]==nums[m-1]:
                l=m+1
            else:
                h=m-1
