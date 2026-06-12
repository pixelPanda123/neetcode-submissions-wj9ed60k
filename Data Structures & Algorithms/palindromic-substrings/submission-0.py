class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = 0

        for i in range(n-1,-1,-1):
            for j in range(n):
                if j >=i: 
                    if s[j]==s[i] and (j-i+1<=2 or dp[i+1][j-1]):
                        dp[i][j] = True 
                        res += 1
        return res 