class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        n = len(nums) 
        low = nums[0]
        mid = float('inf')
        for i in range(1, n):
            if nums[i] <= low:
                low = nums[i]
            elif nums[i] < mid:
                mid = nums[i]
            if nums[i] > mid:
                return True

        return False
            