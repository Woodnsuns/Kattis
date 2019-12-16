# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def traverseSub(root):
            if not root:
                return
            if root.left: traverseSub(root.left)
            result.append(root.val)
            if root.right: traverseSub(root.right)
        traverseSub(root)
        return result