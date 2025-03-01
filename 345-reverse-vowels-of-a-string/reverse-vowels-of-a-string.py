class Solution:
    def reverseVowels(self, s: str) -> str:
        v=['A','a','e','i','o','u','E','I','O','U']
        r=[]
        ans=""
        for i in s:
            if i in v:
                r.append(i)
        for i in s:
            if i in v:
                ans+=(r.pop())
            else:
                ans+=i
        return str(ans)