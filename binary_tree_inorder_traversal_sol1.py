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
        while root:
            if not root.left:
                result.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre and pre.right:
                    pre = pre.right
                temp = root
                pre.right = root
                root = root.left
                temp.left = None
        return result