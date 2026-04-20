class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}

        for i in nums:
            if i in check.keys():
                return True
            else:
                check[i] = 'Found'
        return False
        