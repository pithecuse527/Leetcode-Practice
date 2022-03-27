class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        ans = s[0]
        for i in range(len(s)):
            dp[i][i] = True
            
        for i in range(1, len(s)):
            for j in range(i-1, -1, -1):
                if s[i] == s[j] and (i==j+1 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if len(ans) < len(s[j:i+1]):
                        ans = s[j:i+1]
        return ans