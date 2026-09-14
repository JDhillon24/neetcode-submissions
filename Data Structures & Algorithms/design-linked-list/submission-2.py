class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        head = ListNode(0)
        tail = ListNode(0)

        self.head = head
        self.tail = tail

        self.head.next = tail
        self.tail.prev = head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        cur = self.head.next

        for _ in range(index):
            cur = cur.next
        
        return cur.val

        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        cur = self.head

        for _ in range(index):
            cur = cur.next
        
        new_node = ListNode(val)

        next_node = cur.next
        cur.next = new_node
        new_node.prev = cur
        new_node.next = next_node
        next_node.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        cur = self.head.next

        for _ in range(index):
            cur = cur.next
        
        prev_node = cur.prev
        next_node = cur.next

        prev_node.next = prev_node.next.next
        next_node.prev = prev_node

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)