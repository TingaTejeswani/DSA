class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        n=int(s)
        su=n+1
        r=[]
        su=str(su)
        for i in su:
            r.append(int(i))
        return r