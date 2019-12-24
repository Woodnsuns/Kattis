class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 3)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n+1):
            for j in range(1, i//2 + 1):
                dp[i] = max (
                    dp[i],
                    j * dp[i-j],
                    j*(i-j)
                )
        return dp[n]