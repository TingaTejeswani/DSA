class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s=bin(n)
        s=s[2:]
        s=list(s)
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                return False
        return True
       

                