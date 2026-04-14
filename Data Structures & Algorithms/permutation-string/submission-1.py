class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        s1array = [0]*26 
        windowarray = [0]*26 
        for x in range(len(s1)):
            s1array[ord(s1[x])-ord('a')] += 1 
            windowarray[ord(s2[x])-ord('a')] += 1 
        if s1array == windowarray: 
            return True 
        for x in range(len(s1), len(s2)): 
            windowarray[ord(s2[x-len(s1)])-ord('a')] -=1 
            windowarray[ord(s2[x])-ord('a')] +=1 
            if windowarray == s1array: 
                return True 
        return False 

        