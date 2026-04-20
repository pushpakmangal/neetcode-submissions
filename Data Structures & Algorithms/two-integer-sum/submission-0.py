class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in d.keys():
                return [d[diff], ind]
            else:
                d[val] = ind