# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result = []
        d = -1
        stack = [(root, 0)]
        if not root:
            return result
        while stack:
            node = stack.pop()
            if node[1] > d:
                result.append(node[0].val)
                d = node[1]
            if node[0].left: stack.append((node[0].left, node[1]+1))
            if node[0].right: stack.append((node[0].right, node[1]+1))
        return result
        
        
        