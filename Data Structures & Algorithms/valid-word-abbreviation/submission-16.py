class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p,q=0,0
        while p<len(word) or q<len(abbr):
            print(p, q)
            if p>=len(word):
                return False
            if q< len(abbr) and abbr[q].isalpha():
                if p<len(word) and word[p]!=abbr[q]:
                    return False
                else:
                    p+=1
                    q+=1
            elif abbr[q].isnumeric():
                tmp=q
                flag=False
                while q<len(abbr) and abbr[q].isdigit():
                    if int(abbr[q])==0 and not flag:
                        return False
                    flag=True
                    q+=1
                
                p+=(int(abbr[tmp:q]))
                if p==len(word) and q==len(word):
                    return True
                if p>len(word):
                    return False

        return True