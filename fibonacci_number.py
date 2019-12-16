class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        dp = [-1 for _ in range(N+1)]
        dp[0] = 0
        dp[1] = 1
        
        n = 2
        while n <= N:
            #print n
            dp[n] = dp[n-1] + dp[n-2]
            n += 1
        return dp[n-1]
                
        