import math 
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        for x, y in points: 
            dist = -1*(x**2 + y**2)
            heapq.heappush(maxHeap, [dist, x ,y])
            if len(maxHeap) >k: 
                heapq.heappop(maxHeap)
        while maxHeap: 
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
