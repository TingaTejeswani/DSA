class Solution:
    from itertools import permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        s=permutations(nums)
        r=[]
        for i in s:
            r.append(i)
        return r

        