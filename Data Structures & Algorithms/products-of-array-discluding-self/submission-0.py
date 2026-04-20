class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, res = [], [], []
        mul = 1
        for i in range(len(nums)):
            mul*=nums[i]
            pre.append(mul)
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            mul*=nums[i]
            post.insert(0, mul)

        for i in range(len(nums)):
            if i==0:
                val = 1*post[i+1]
            elif i==(len(nums)-1):
                val = pre[i-1]*1
            else:
                val = pre[i-1]*post[i+1]
            res.append(val)
        return res        
        