# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        def findHeight(root):
            h = 0
            while root.left:
                h += 1
                root = root.left
            return h
        
        def search(idx, h, root):
            leftmax = pow(2, h-1) 
            while h > 0:
                if idx < leftmax:
                    root = root.left
                if idx >= leftmax:
                    idx = idx - leftmax
                    root = root.right
                h -= 1
                leftmax = pow(2, h-1)
            return root
        
        h = findHeight(root)
        llmax = pow(2, h)-1
        llmin = 0
        mid = (llmax + llmin) / 2
        while llmax > llmin:
            pivot = search(mid, h, root)
            if not pivot:
                mid -= 1
                llmax = mid
            else:
                if search(mid+1, h, root):
                    llmin = mid + 1
                else:
                    break
            mid = (llmax + llmin) // 2
    
        return mid + 1 + pow(2, h) - 1
        
        