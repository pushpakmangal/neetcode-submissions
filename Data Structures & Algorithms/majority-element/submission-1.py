class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val=nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i]==val:
                cnt+=1
            else:
                if cnt>0:
                    cnt-=1
                else:
                    val=nums[i]
                    cnt+=1

        return val


        