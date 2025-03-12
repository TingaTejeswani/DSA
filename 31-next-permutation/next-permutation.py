class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        j=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                j=i
                break
        if j==-1:
            nums.reverse()
            return 
        for i in range(n-1,j,-1):
            if nums[i]>nums[j]:
                k=i
                break
        nums[j],nums[k]=nums[k],nums[j]
        nums[j+1:]=reversed(nums[j+1:])