class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount,scount={},{}
        
        for char in t:
            tcount[char]=1+tcount.get(char,0)
        have,need=0,len(tcount.keys())

        res=[]
        minl=len(s)
        l=0
        for r in range(len(s)):
            if s[r] in tcount.keys():
                scount[s[r]]=1+scount.get(s[r],0)
                if scount[s[r]]==tcount[s[r]]:
                    have+=1
            if have==need:
                while l<=r and have==need:
                    if (r-l+1)<=minl:
                        minl=r-l+1
                        res.append([l,r])
                    if s[l] in tcount.keys():
                        scount[s[l]]-=1
                        if scount[s[l]]<tcount[s[l]]:
                            have-=1
                    l+=1
        if len(res)==0: return ""
        l,r=res[-1][0],res[-1][1]
        return s[l:r+1]
            

                

        