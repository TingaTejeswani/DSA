class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=[]
        for i in nums:
            if i!=0:
                s.append(i)
        for i in range(len(s),len(nums)):
            s.append(0)
        idx=0
        for i in range(len(nums)):
            nums[i]=s[idx]
            idx+=1
        
