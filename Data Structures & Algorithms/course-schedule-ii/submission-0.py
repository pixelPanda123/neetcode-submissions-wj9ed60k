class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i :[] for i in range(numCourses)}
        for crs, preq in prerequisites: 
            premap[crs].append(preq)
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle: 
                return False 
            if crs in visit: 
                return True 
            cycle.add(crs)
            for preq in premap[crs]:
                if not dfs(preq):
                    return False 
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True 
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
        
