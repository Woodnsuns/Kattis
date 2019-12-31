class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = set()
        for num in nums:
            used.add(num)
        def helper(nums):
            if len(nums) == 0:
                return []
            if len(nums) == 1:
                return [nums]
            used = set()
            res = []
            for i, num in enumerate(nums):
                if num not in used:
                    for p in helper(nums[:i] + nums[i+1:]):
                        res.append([num] + p)
                    used.add(num)
            return res
        return helper(nums)
                    
            
            