class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)
        for n in nums:
            count[n]+=1
            if len(count)<=2:
                continue
            new_count=defaultdict(int)
            for val,c in count.items():
                if count[val]>1:
                    new_count[val]=c-1

            count=new_count
        
        res=[]
        for val in count:
            if nums.count(val)>(len(nums)//3):
                res.append(val)

        return res

        