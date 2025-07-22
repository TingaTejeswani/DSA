class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        b=0
        r=[]
        st=0
        for i,c in enumerate(s):
            if c=='(':
                b+=1
            elif c==')':
                b-=1
            if b==0:
                r.append(s[st+1:i])
                st=i+1
        return ''.join(r)
