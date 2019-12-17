# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tonext = 0
        head = None
        prev = None
        while True:
            
            if not l1 and not l2 and tonext == 0:
                break
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            d = a + b + tonext
            #print("a = {}, b = {}, d = {}".format(a, b, d))
            if d >= 10:
                tonext = 1
                d -= 10
            else:
                tonext = 0
            current = ListNode(d)
            
            if prev:
                prev.next = current
            else:
                head = current
            
            prev = current
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return head
        