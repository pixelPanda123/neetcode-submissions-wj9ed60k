class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): 
            return False 
        for x in range(len(s2)-(len(s2)%len(s1))):
            curr = s2[x:x+len(s1)]
            if sorted(curr) == sorted(s1):
                return True 
        return False 
        

        