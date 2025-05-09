class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=bin(n)
        s=s[2:]
        p=''
        for i in s:
            if i=='1':
                p+='0'
            else:
                p+='1'
        return int(p,2)
                