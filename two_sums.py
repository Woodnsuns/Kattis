class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = dict()
        
        for i, val in enumerate(nums):
            if val not in num_to_index:
                num_to_index[val] = list()
            num_to_index[val].append(i)
        
        nums.sort()
        i = 0
        j = len(nums) - 1
        while (j > i):
            if nums[i] + nums[j] == target:
                return [num_to_index[nums[i]].pop(0), num_to_index[nums[j]].pop(0)]
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        
            
        