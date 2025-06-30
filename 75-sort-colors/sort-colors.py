class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        if len(nums)==1:
            return nums
        else:
            c1=0
            c2=0
            c=0
            for i in nums:
                if i==0:
                    c+=1
                elif i==1:
                    c1+=1
                else:
                    c2+=1
            for i in range(c):
                nums[i]=0
            for i in range(c,c+c1):
                nums[i]=1
            for i in range(c+c1,len(nums)):
                nums[i]=2
            return nums
            