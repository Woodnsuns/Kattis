# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(head1, head2, len1, len2):
            head = None
            prev = None
            if len1 == 0:
                return head2
            elif len2 == 0:
                return head1
            if head1.val < head2.val:
                head = head1
                head1 = head1.next
                len1 -= 1
            else:
                head = head2
                head2 = head2.next
                len2 -= 1
            prev = head
            while len1 > 0 and len2 > 0:
                if head1.val < head2.val:
                    prev.next = head1
                    head1 = head1.next
                    len1 -= 1
                else:
                    prev.next = head2
                    head2 = head2.next
                    len2 -= 1
                prev = prev.next
            if len1 > 0:
                prev.next = head1

            if len2 > 0:
                prev.next = head2

            return head
                    
            
            
            
        def mergeSort(head, len):
            if len <= 1:
                return head
            else:
                len1 = len // 2
                len2 = len - len1
                tail1 = head1 = head
                for i in range(len1-1):
                    tail1 = tail1.next
                head2 = tail1.next
                tail1.next = None
                head1 = mergeSort(head1, len1)
                head2 = mergeSort(head2, len2)
                head = merge(head1, head2, len1, len2)
                return head
                
            
        tail = head
        n = 0
        while tail:
            tail = tail.next
            n += 1
        head = mergeSort(head, n)
        return head