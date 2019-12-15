# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def makeSubtree(i0, i1, N):
            if N <= 0:
                return None
            root = TreeNode(pre[i0])
            if N == 1:
                return root
            for L in range(N):
                if post[i1+L-1] == pre[i0+1]:
                    break
            root.left = makeSubtree(i0+1, i1, L)
            root.right = makeSubtree(i0+1+L, i1+L, N-1-L)
            return root
        return makeSubtree(0, 0, len(pre))
        