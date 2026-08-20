class Solution:
    def check_freq(self, freq):
        count={}
        for char in freq:
            count[char]=1+count.get(char,0)
        return count

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq=self.check_freq(s1)
        s2_freq={}
        if len(s2)<len(s1):
            return False
        l,r=0,len(s1)-1
        while l<len(s2) and r<len(s2):
            print(l,r)
            if l==0:
                for i in range(l,r+1):
                    s2_freq[s2[i]]=1+s2_freq.get(s2[i],0)
            else:
                s2_freq[s2[l-1]]-=1
                if s2_freq[s2[l-1]]==0:
                    s2_freq.pop(s2[l-1])
                s2_freq[s2[r]]=1+s2_freq.get(s2[r],0)
            print(s1_freq,s2_freq)
            if s1_freq==s2_freq:
                return True
            l+=1
            r+=1
        return False


             


                



        