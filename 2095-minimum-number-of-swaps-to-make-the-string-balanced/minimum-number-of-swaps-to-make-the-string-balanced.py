class Solution:
    def minSwaps(self, s: str) -> int:
        mu=0
        b=0
        for i in s:
            if i=='[':
                b+=1
            else:
                b-=1
                mu=max(mu,-b)
        return (mu+1)//2