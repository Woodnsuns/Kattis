# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        result = []
        if not root:
            return result
        while stack:
            node = stack.pop()
            result.append(node.val)
            #print node
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return result