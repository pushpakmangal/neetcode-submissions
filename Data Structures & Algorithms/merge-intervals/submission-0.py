class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        out=[intervals[0]]
        for s,e in intervals:
            laste=out[-1][1]
            if laste>=s:
                out[-1][1]=max(laste,e)
            else:
                out.append([s,e])
        return out
            

        