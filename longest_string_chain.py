class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        def isSubsequence(shorter, longer):
            if len(longer) - len(shorter) != 1:
                return False
            i, j = 0, 0
            for i in range(len(shorter)):
                if longer[j] != shorter[i]:
                    longer = longer[:j] + longer[j+1:]
                    if longer != shorter:
                        return False
                j += 1
            return True
        
        if len(words) <= 1:
            return 1
        words.sort(key=len)
        dp = [1] * len(words)
        maxlen = 1
        
        for i in range(len(words)):
            cur = words[i]
            j = i - 1
            while j > 0 and len(words[j]) >= len(words[i]):
                j -= 1
            while j >= 0 and len(words[j]) == len(words[i]) - 1:
                if isSubsequence(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > maxlen:
                        maxlen = dp[i]
                j -= 1
        return maxlen