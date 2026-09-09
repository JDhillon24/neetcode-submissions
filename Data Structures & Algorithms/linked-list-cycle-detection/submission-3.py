# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_map = {}
        index = 0
        cur = head

        while cur:
            if cur in seen_map:
                return True
        
            seen_map[cur] = index
            index += 1

            cur = cur.next
        
        return False


        