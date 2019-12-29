class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        memo = [0] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(memo[0], nums[1])
        for i in range(2, len(nums)):
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        return memo[len(nums) - 1]