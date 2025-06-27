class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=set()
        c=0
        for i in nums:
            if i not in p:
                p.add(i)
                nums[c]=i
                c+=1

        return c