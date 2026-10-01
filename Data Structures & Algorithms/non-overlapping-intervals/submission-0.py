class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        lastEnd=intervals[0][1]
        res=0

        for interval in intervals[1:]:
            s,e=interval[0],interval[1]
            if s>=lastEnd:
                lastEnd=e
            else:
                res+=1
                lastEnd=min(lastEnd, e)
        return res
