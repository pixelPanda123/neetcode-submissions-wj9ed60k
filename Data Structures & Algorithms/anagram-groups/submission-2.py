class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs: 
            if str(sorted(x)) not in hashmap: 
                hashmap[str(sorted(x))] = [x]
            else: 
                hashmap[str(sorted(x))].append(x)
        return list(hashmap.values())
        