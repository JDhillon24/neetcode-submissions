# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = ListNode()
        slow = head
        fast = head
        count = 0

        while count < n:
            fast = fast.next
            count += 1
        
        while fast:
            prev.next = slow
            slow = slow.next
            fast = fast.next
            prev = prev.next
        

        prev.next = slow.next

        if slow == head:
            return slow.next
        else:
            return head

        