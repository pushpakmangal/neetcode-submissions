class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        k=max(piles)
        while l<=r:
            mid=l+(r-l)//2
            total_hours=0
            for val in piles:
                total_hours+=math.ceil((float(val))/mid)

            if total_hours<=h:
                k=mid
                r=mid-1
            else:
                l=mid+1
        return k
            

            

                

        