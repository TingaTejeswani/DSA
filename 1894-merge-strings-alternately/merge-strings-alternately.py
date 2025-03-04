class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r=""
        n=min(len(word1),len(word2))
        for i in range(n):
            r+=word1[i]+word2[i]
        return r+word1[n:]+word2[n:]