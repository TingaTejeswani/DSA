class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        md=0
        for i in s:
            if i=='(':
                c+=1
                md=max(md,c)
            elif i==')':
                c-=1
        return md