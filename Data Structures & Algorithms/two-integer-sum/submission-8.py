class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pos={}
        for ind,num in enumerate(nums):
            val=target-num
            # print(pos, val)
            if val in pos.keys():
                return [pos[val], ind]
            else:
                pos[num]=ind


        