class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        h=sum(nums)
        while l<=h:
            m=(l+h)//2
            c=1
            t=0
            for i in nums:
                if  t+i>m:
                    c+=1
                    t=i
                else:
                    t+=i
            if c<=k:
                h=m-1
            else:
                l=m+1
        return l
        