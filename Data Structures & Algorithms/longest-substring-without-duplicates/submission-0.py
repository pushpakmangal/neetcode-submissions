class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        check=set()
        maxL=0
        l,r=0,0
        while l<len(s) and r<len(s):
            if s[r] not in check:
                check.add(s[r])
                maxL=max(maxL,(r-l+1))
                r+=1
            else:
                check.remove(s[l])
                l+=1
        return maxL

        

