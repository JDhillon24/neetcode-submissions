class ListNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)
        
        

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        new_node.prev = self.cur
        self.cur.next = new_node
        self.cur = new_node
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.prev is None:
                return self.cur.val
            
            self.cur = self.cur.prev
        
        return self.cur.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.next is None:
                return self.cur.val
            
            self.cur = self.cur.next
        
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)