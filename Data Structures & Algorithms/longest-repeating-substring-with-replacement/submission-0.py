class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        l,r=0,0
        ans=0
        maxf=0
        while r<len(s):
            count[s[r]]+=1
            maxf=max(maxf,count[s[r]])
            # print(l, r, window, count, maxTill, ans)
            if (r-l+1)-maxf<=k:
                ans=max(ans,r-l+1)
            else:
                count[s[l]]-=1
                l+=1
            r+=1
        return ans
            


        