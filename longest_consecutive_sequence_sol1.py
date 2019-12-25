class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        memo = {}
        longest = 0
        for num in nums:
            if num in memo:
                continue
            l = memo[num - 1] if num - 1 in memo else -1
            r = memo[num + 1] if num + 1 in memo else -1
            newlen = 1
            if l == -1 and r == -1:
                memo[num] = 1
            if l != -1 and r != -1:
                memo[num - l] = memo[num + r] = memo[num] = l + r + 1
                newlen = l + r + 1
            elif l != -1:
                memo[num] = memo[num - l] = l + 1
                newlen = l + 1
            elif r != -1:
                memo[num + r] = memo[num] = r + 1
                newlen = r + 1
            longest = max(newlen, longest)
                
        return longest
        
            
                
                