# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        dummy = ListNode(None)

        while head:
            next = head.next
            if next == dummy:
                return True
            head.next = dummy
            head = next
        
        return False


        