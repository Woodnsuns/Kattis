class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = dict()
        
        for i, val in enumerate(nums):
            if val in num_to_index:
                if target == val + val:
                    return [num_to_index[val], i]

            num_to_index[val] = i
        
        for i in range(len(nums)):
            dif = target - nums[i]
            print ("dif = {}".format(dif))
            if dif in num_to_index and num_to_index[dif] != i:
                return [num_to_index[dif], i]
            
        
        
        
            
        