class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1 or nums[0]<nums[-1]:
            return nums[0]
        res=nums[0]
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            res=min(res,nums[mid])
            if nums[l]<nums[r]:
                return min(res,nums[l])
            elif nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1
        return res



            





        