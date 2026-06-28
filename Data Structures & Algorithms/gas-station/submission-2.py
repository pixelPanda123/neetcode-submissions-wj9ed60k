class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)< sum(cost):
            return -1 
        res = 0 
        diff = 0 
        n = len(gas)
        for i in range(n):
            diff += gas[i]-cost[i]
            if diff <0: 
                res = i +1 
                diff = 0 
        return res 