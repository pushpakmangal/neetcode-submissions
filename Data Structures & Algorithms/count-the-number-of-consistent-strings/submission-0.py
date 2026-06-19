class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        cnt=0
        for word in words:
            notAllowed=False
            for char in word:
                if char not in a:
                    notAllowed=True
                    break
            if not notAllowed:
                cnt+=1
        return cnt

                    
        