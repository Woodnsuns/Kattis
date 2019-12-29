# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def robSubtree(root):
            res = [0, 0]
            if not root:
                return res
            left = robSubtree(root.left)
            right = robSubtree(root.right)
            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = root.val + left[0] + right[0]
            
            return res
                
        res = robSubtree(root)
        return max(res[0], res[1])