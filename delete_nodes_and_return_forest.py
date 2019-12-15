# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        result = []
        queue = []
        to_delete = set(to_delete)
        left = 0
        right = 1
        def delSubnodes(node, nodep, l_or_r):
            if not node:
                return 
            delSubnodes(node.left, node, left)
            delSubnodes(node.right, node, right)
            if node.val in to_delete:
                if l_or_r == left:
                    nodep.left = None
                elif l_or_r == right:
                    nodep.right = None
                if node.left: 
                    result.append(node.left)
                if node.right: 
                    result.append(node.right)
        delSubnodes(root, None, -1)
        if not (root.val in to_delete): result.append(root)

        return result
            
            
            
            
        
        