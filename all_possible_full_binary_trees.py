# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        memo = {0: [], 1: [TreeNode(0)]}
        for n in xrange(3, N + 1, 2):
            ans = []
            for x in xrange(1, n - 1, 2):
                y = n - x - 1
                for left in memo[x]:
                    for right in memo[y]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            print n
            memo[n] = ans
        return memo[N]
        
                
                
                
        