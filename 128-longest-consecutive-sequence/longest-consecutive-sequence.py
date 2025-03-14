class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            c=1
            ans=1
            for i in range(1,n):
                if nums[i]-nums[i-1]==1:
                    c+=1
                    ans=max(ans,c)
                elif nums[i]==nums[i-1]:
                    continue
                else:
                    c=1
        return ans