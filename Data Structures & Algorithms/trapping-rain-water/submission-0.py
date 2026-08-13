class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        l,r=1,len(height)-2
        maxL,maxR=height[l-1],height[r+1]
        res=0

        while l<=r:
            if maxL<=maxR:
                val=min(maxL,maxR)-height[l]
                if val>0:
                    res+=val
                maxL=max(maxL,height[l])
                l+=1
            else:
                val=min(maxL,maxR)-height[r]
                if val>0:
                    res+=val
                maxR=max(maxR,height[r])
                r-=1
        return res



        