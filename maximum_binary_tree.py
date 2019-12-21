# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) <= 0:
            return
        curroot = TreeNode(nums[0])
        for i in range(1, len(nums)):
            newnode = TreeNode(nums[i])
            if nums[i] > curroot.val:
                newnode.left = curroot
                curroot = newnode
            else:
                nodeptr = curroot
                while nodeptr.right and nodeptr.right.val >= nums[i]:
                    nodeptr = nodeptr.right
                newnode.left = nodeptr.right
                nodeptr.right = newnode
        return curroot
            
                
                
        