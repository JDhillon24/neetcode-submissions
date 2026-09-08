# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node to start as head
        dummy = ListNode()

        # tail to track latest node
        tail = dummy

        # pointers to track each list
        cur1 = list1
        cur2 = list2

        # iterating through list
        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            
            # advance tail pointer
            tail = tail.next
        
        # one or both lists have been exhausted so setting next to remaining items
        tail.next = cur1 if cur1 else cur2

        return dummy.next



