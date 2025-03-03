class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        w=s[-1]
        c=0
        for i in w:
            c+=1
        return c