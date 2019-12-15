# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValidSub(root, min, max):
            if not root:
                return True
            if min and root.val <= min.val:
                return False
            if max and root.val >= max.val:
                return False
            return isValidSub(root.left, min, root) and isValidSub(root.right, root, max)
        return isValidSub(root, None, None)
        