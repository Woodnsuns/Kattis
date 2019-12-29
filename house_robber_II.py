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
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def tryInRange(i, j):
            memo = [0] * len(nums)
            for k in range(i, j + 1):
                if k - 2 >= 0:
                    memo[k] = max(nums[k] + memo[k - 2], memo[k - 1])
                else:
                    memo[k] = max(nums[k], nums[i])
            return memo[j]
        return max(tryInRange(0, len(nums) - 2), tryInRange(1, len(nums) - 1))
