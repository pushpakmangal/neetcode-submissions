class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums=sorted(nums)
        # nums=[-4, -1, -1, 0, 1, 2]
        for ind,num in enumerate(nums):
            if ind>0 and nums[ind]==nums[ind-1]:
                continue

            l,r=ind+1,len(nums)-1
            while l<r:
                val=num+nums[l]+nums[r]
                if val>0:
                    r-=1
                elif val<0:
                    l+=1
                else:
                    res.append([num, nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

                
                
            


        