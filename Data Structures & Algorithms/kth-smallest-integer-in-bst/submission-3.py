# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cnt = k
        res = root.val

        def kthSmallestHelper(root: Optional[TreeNode]) -> None:
            nonlocal cnt, res
            if not root:
                return
        
        
            kthSmallestHelper(root.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = root.val
                return
            kthSmallestHelper(root.right)

        kthSmallestHelper(root)

        return res
        