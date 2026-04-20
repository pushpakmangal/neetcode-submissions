class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for val in nums:
            freq[val] = 1 + freq.get(val, 0)

        bucket = [[] for i in range(len(nums)+1)]

        for val, cnt in freq.items():
            bucket[cnt].append(val)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res

        