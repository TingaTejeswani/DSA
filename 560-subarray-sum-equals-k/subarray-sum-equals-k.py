class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p={0:1}
        ps=0
        c=0
        for i in nums:
            ps+=i
            if ps-k in p:
                c+=p[ps-k]
            if ps in p:
                p[ps]+=1
            else:
                p[ps]=1
        return c