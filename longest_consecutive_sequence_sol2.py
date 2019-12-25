class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxstreak = 0
        for num in nums:
            if num - 1 not in nums:
                cur = num + 1
                curstreak = 1
                while cur in nums:
                    cur += 1
                    curstreak += 1
                maxstreak = max(maxstreak, curstreak)
        return maxstreak
                    
        
            
                
                