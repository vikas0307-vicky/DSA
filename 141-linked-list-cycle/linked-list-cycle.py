# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # "Floyads cycle"
        # fast and close 
        # fast = 2 steps at a time
        # slow  =1 step at a time

        fast  =  head
        slow  =  head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                return True
        return False


        