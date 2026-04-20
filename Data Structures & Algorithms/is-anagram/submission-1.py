class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}

        for val in s:
            if val in a.keys():
                a[val]+=1
            else:
                a[val]=0

        for val in t:
            if val in b.keys():
                b[val]+=1
            else:
                b[val]=0

        return a==b


        