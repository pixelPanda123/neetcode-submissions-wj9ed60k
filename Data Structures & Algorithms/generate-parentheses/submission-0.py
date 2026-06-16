class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []  
        def dfs(opend, close): 
            if opend == close == n: 
                ans.append("".join(stack))
                return 
            if opend<n:
                stack.append("(")
                dfs(opend+1, close)
                stack.pop()
            if close<opend: 
                stack.append(")")
                dfs(opend,close+1)
                stack.pop()
        dfs(0,0)
        return ans




        