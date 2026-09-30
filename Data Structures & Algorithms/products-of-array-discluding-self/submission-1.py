class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre,post=1,1
        res=[1]*len(nums)
        for i in range(len(nums)-1):
            pre*=nums[i]
            res[i+1]=pre

        for i in range(len(nums)-1, 0, -1):
            post*=nums[i]
            res[i-1]*=post

        return res



        