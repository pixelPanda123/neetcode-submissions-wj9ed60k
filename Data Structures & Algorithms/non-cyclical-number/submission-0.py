class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: 
            return True 
        visit = set()
        while n and n not in visit:
            visit.add(n)
            sum = 0 
            while n: 
                rem = n%10 
                sum += rem**2 
                n = n//10 
            n = sum 
            if n == 1: 
                return True 
                break 
        return False 