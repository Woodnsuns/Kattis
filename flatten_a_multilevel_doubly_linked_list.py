"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        def dfs(head):
            if head.child:
                tail = dfs(head.child)
                if head.next:
                    tail.next = head.next
                    head.next.prev = tail
                head.next = head.child
                head.child.prev = head
                head.child = None
                
            if not head.next:
                return head
            else:
                return dfs(head.next)
        dfs(head)
        return head
            
        