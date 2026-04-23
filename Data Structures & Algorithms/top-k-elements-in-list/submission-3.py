class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ans = []
        for x in nums: 
            if x in hashmap: 
                hashmap[x]+=1 
            else: 
                hashmap[x] =1 
        sd = sorted(hashmap.items(), key=lambda x:(-x[1], x[0]))
        for i in range(k):
            ans.append(sd[i][0])
        return ans

        