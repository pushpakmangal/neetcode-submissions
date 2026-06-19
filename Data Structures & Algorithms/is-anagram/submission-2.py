class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        d={}
        e={}
        for char in s:
            d[char]=1+d.get(char,0)

        for char in t:
            e[char]=1+e.get(char,0)

        if d==e:
            return True
        return False

        