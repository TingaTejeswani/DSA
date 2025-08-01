class Solution:
    def frequencySort(self, s: str) -> str:
        p={}
        for i in s:
            if i in p:
                p[i]+=1
            else:
                p[i]=1
        l=[]
        for i in p:
            l.append((p[i],i))
        l.sort(reverse=True)
        r=""
        for i,v in l:
            r+=i*v
        return r