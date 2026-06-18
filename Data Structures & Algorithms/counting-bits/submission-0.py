class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            ones = 0 
            for j in range(32):
                mask =  1<<j 
                if mask&i : 
                    ones += 1 
            res.append(ones)
        return res
        