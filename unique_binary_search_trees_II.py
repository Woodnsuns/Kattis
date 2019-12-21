# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        if n == 1:
            return [TreeNode(n)]
        def generateSubTrees(start, end):
            if start > end:
                return [None]
            result = []
            for i in range(start, end+1):
                left_trees = generateSubTrees(start, i-1)
                right_trees = generateSubTrees(i+1, end)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        result.append(root)
            return result
        return generateSubTrees(1, n)
                