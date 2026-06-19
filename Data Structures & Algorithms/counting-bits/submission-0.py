class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOne(num):
            cnt=0
            while num:
                if num%2==1:
                    cnt+=1
                num=num//2
            return cnt

        result=[]
        for i in range(n+1):
            result.append(countOne(i))

        return result



        