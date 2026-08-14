class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA=0
        stack=[]

        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>=h:
                ind,v=stack.pop()
                maxA=max(maxA,(i-ind)*v)
                start=ind
            stack.append((start,h))

        while stack:
            ind,v=stack.pop()
            maxA=max(maxA,(len(heights)-ind)*v)
            
        
        return maxA




        