class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for interval in intervals: 
            if res: 
                prev = res.pop()
                if prev[0]<=interval[0]<=prev[1]:
                    prev[0] = min(prev[0], interval[0])
                    prev[1] = max(prev[1], interval[1])
                    res.append(prev)
                else: 
                    res.append(prev)
                    res.append(interval)
            else: 
                res.append(interval)
        return res 
        