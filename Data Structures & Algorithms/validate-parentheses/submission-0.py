class Solution:
    def isValid(self, s: str) -> bool:
        check={
            ')': '(',
            ']': '[',
            '}': '{'
        }
        lst=[]
        for char in s:
            if char in check.keys():
                if lst and check[char]==lst[-1]:
                    lst.pop()
                else:
                    return False
                
            else:
                lst.append(char)
        if not lst:
            return True
        return False

        