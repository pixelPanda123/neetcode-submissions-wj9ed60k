class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*(len(s)+1) for _ in range(len(s)+1)]
        n = len(s)
        residx = -1 
        reslength = 0 
        for i in range(n-1,-1,-1):
            for j in range(0,n):
                if (s[i]==s[j]) and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True 
                    curr = j-i+1
                    if curr>reslength: 
                        reslength = curr 
                        residx = i 
        return s[residx:residx+reslength]




        