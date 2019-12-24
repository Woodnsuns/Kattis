# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        def getLength(root):
            n = 0
            cur = root
            while cur:
                cur = cur.next
                n += 1
            return n
        
        n = getLength(root)
        m = n//k
        rem = n % k
        cur = root
        result = [None] * k
        j = 0
        while cur:
            i = m + 1 if rem > 0 else m
            result[j] = cur
            while i > 1:
                cur = cur.next
                i -= 1
            temp = cur.next
            cur.next = None
            cur = temp
            j += 1
            rem -= 1
        return result