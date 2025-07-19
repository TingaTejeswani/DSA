class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s={}
        l=[]
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        for i,j in s.items():
            if j>len(nums)//3:
                l.append(i)
        return l
