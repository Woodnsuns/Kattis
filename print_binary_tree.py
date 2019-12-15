# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        nlist = []
        
        def findMaxDepth(root):
            if root == None:
                return 0
            else:
                return 1 + max(findMaxDepth(root.left), findMaxDepth(root.right))
        
        d = findMaxDepth(root)
        result = [["" for j in range(pow(2, d-1)*2-1)] for i in range(d)]
        l = len(result[0]) / 2
        
        def printVal(root, s, l, d):
            if not root:
                return 
            #print ("l = {}".format(l))
            result[d][s+l] = str(root.val)
            s1 = s
            s2 = s + l + 1
            l = l / 2
            printVal(root.left, s1, l, d+1)
            printVal(root.right, s2, l, d+1)
        printVal(root, 0, l, 0)
        return result
        
            