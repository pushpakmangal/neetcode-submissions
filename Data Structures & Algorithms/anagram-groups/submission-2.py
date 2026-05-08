class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check=defaultdict(list)
        
        for word in strs:
            check["".join(sorted(word))].append(word)

        return list(check.values())
        