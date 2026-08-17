class TimeMap:

    def __init__(self):
        self.s=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.s[key]:
            return ""
        ans=""
        lst=self.s[key]
        l,r=0,len(lst)-1
        while l<=r:
            mid=l+(r-l)//2
            if lst[mid][1]==timestamp:
                return lst[mid][0]
            elif lst[mid][1]>timestamp:
                r=mid-1
            else:
                ans=lst[mid][0]
                l=mid+1
        return ans


                



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)