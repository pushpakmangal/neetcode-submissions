class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        i,j=0,1
        while j<len(prices):
            if prices[i]<prices[j]:
                diff=prices[j]-prices[i]
                profit=max(profit,diff)
            else:
                i=j
            j+=1
        return profit
            
        