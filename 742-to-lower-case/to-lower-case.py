class Solution:
    def toLowerCase(self, s: str) -> str:
        t=''
        for i in s:
            if 64<ord(i)<91:
                i=chr(ord(i)+32)
                t+=i
            else:
                t+=i
        return t
            