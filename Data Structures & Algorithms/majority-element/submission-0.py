class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=defaultdict(int)

        for num in nums:
            count[num]+=1

        maxVal,maxCnt=0,0
        for val,cnt in count.items():
            if cnt>maxCnt:
                maxCnt=cnt
                maxVal=val
        return maxVal

        