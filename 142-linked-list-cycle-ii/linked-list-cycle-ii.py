class Solution:
    def detectCycle(self, head):
        # "Slow" = l1+l2
        # "Fast" = l1+l2
        # 2(l1+l2) = l1+l2 -nk
        # l1+l2 = nk 
        # l1 = l1


        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None