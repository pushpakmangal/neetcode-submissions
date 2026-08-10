class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        profit=0
        while r<len(prices):
            tmp=prices[r]-prices[l]
            profit+=max(0,tmp)
            l=r
            r+=1
        return profit


        