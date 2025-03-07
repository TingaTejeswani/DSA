class Solution:
    def firstUniqChar(self, s: str) -> int:
        l={}
        for char in s:
            l[char]=l.get(char,0)+1
        for i,char in enumerate(s):
            if l[char]==1:
                return i
        return -1