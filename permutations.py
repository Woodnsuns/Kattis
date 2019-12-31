class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums):
            if len(nums) <= 0:
                return []
            if len(nums) == 1:
                return [nums]
            res = []
            for i in range(len(nums)):
                num = nums[i]
                for p in helper(nums[:i] + nums[i+1:]):
                    res.append([num] + p)
            return res
        return helper(nums)