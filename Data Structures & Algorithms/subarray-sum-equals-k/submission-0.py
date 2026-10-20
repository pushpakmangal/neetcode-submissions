class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,num=0,0
        prefix={0:1}
        for i in range(len(nums)):
            num+=nums[i]
            if num-k in prefix.keys():
                res+=prefix[num-k]
            prefix[num]=1+prefix.get(num, 0)
        return res



        