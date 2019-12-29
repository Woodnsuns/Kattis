from operator import truediv, mul, add, sub
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                num1 = nums[i]
                for j in range(i + 1, len(nums)):
                    if i == j:
                        continue
                    num2 = nums[j]
                    combs = {mul(num1, num2), mul(num2, num1), add(num1, num2), sub(num1, num2), sub(num2, num1)}
                    if num2 != 0:
                        combs.add(truediv(num1, num2))
                    if num1 != 0:
                        combs.add(truediv(num2, num1))
                    
                    for comb in combs:
                        arr = []
                        for k in range(len(nums)):
                            if k != i and k != j:
                                arr.append(nums[k])
                        arr.append(comb)
                        if helper(arr):
                            return True
            return False
        return helper(nums)
                