class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        p={}
        tt={}
        for i in range(len(s)):
            if s[i] not in p:
                p[s[i]]=i
            if t[i] not in tt:
                tt[t[i]]=i
            if p[s[i]]!=tt[t[i]]:
                return False
        
        return True
            