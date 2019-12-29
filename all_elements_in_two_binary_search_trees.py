# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def flattern(root):
            result = []
            cur = root
            while cur:
                if not cur.left:
                    result.append(cur.val)
                    cur = cur.right
                else:
                    pre = cur.left
                    while pre.right:
                        pre = pre.right
                    pre.right = cur
                    temp = cur.left
                    cur.left = None
                    cur = temp
            return result
        res1 = flattern(root1)
        res2 = flattern(root2)
        result = []
        i, j= 0, 0
        while i < len(res1) and j < len(res2):
            if res1[i] < res2[j]:
                result.append(res1[i])
                i += 1
            else:
                result.append(res2[j])
                j += 1
        while i < len(res1):
            result.append(res1[i])
            i += 1
        while j < len(res2):
            result.append(res2[j])
            j += 1
        return result
            
            
        