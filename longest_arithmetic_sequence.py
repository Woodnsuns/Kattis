class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n <= 2:
            return 2
        
        dp = [{}, {A[1] - A[0]: 2}]
        maxlen = 2
        for i in range(2, n):
            j = i - 1
            dp.append(dict())
            while j >= 0:
                d = A[i] - A[j]
                if d in dp[j]:
                    if d not in dp[i] or (d in dp[i] and dp[i][d] < dp[j][d] + 1):
                        dp[i][d] = dp[j][d] + 1
                        maxlen = max(dp[i][d], maxlen)
                elif d not in dp[i]:
                    dp[i][d] = 2
                j -= 1
        return maxlen
                    
        
                    
        