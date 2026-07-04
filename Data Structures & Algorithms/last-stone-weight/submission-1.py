import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones: 
            heapq.heappush(maxHeap, -1*stone)
        while len(maxHeap) >1: 
            e1 = heapq.heappop(maxHeap)
            e2 = heapq.heappop(maxHeap)
            diff = abs(e1-e2)
            if diff >0:
                heapq.heappush(maxHeap, -1*diff)
        maxHeap.append(0)
        return abs(maxHeap[0])