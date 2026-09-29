# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode
        tail = dummy
        carry = 0


        while l1 and l2:
            num = l1.val + l2.val + carry
            new_node = ListNode(num % 10)
            carry = num // 10

            tail.next = new_node
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
        
        while l1:
            num = l1.val + carry
            new_node = ListNode(num % 10)
            carry = num // 10

            tail.next = new_node
            l1 = l1.next
            tail = tail.next
        
        while l2:
            num = l2.val + carry
            new_node = ListNode(num % 10)
            carry = num // 10

            tail.next = new_node
            l2 = l2.next
            tail = tail.next

        if carry:
            tail.next = ListNode(carry)
        
        return dummy.next