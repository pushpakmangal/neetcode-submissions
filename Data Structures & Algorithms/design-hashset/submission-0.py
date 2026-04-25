class MyHashSet:

    def __init__(self):
        self.lst = []

    def add(self, key: int) -> None:
        if key not in self.lst:
            self.lst.append(key)
        

    def remove(self, key: int) -> None:
        self.final=[]
        for num in self.lst:
            if num!=key:
                self.final.append(num)
        self.lst = self.final
        

    def contains(self, key: int) -> bool:
        if key in self.lst:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)