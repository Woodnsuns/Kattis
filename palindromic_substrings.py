class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = len(s)
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1:
                if s[i] == s[i+1]:
                    dp[i][i+1] = 1
                    total += 1
            
        for span in range(2, len(s)):
            for left in range(len(s) - span):
                right = left + span
                if dp[left+1][right-1] == 1:
                    if s[left] == s[right]:
                        dp[left][right] = 1
                        total += 1
        return total
        
            
                
                
        