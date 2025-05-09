class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)
        s=s[2:]
        p=''
        for i in s:
            if i=='0':
                i='1'
                p+=i
            else:
                i='0'
                p+=i
        return int(p,2)
        