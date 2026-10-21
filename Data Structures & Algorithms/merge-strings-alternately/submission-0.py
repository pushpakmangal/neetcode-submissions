class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f,s=0,0
        res=""
        while f<len(word1) or s<len(word2):
            if f<len(word1):
                res+=word1[f]
            if s<len(word2):
                res+=word2[s]
            f+=1
            s+=1

        return res


        